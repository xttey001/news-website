#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
板块轮动监控提醒系统
实时监控芯片/医药/电网设备板块，自动识别轮动信号并提醒
"""

import requests
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import logging

# 导入通知模块
try:
    from notification_extensions import (
        MultiChannelNotifier, 
        FeishuNotification,
        create_notifier_from_config
    )
    NOTIFICATION_AVAILABLE = True
except ImportError:
    NOTIFICATION_AVAILABLE = False
    print("⚠️ 通知模块未找到，将只使用控制台输出")

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sector_monitor.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class SectorRotationMonitor:
    """板块轮动监控器"""
    
    def __init__(self):
        # 监控标的配置
        self.watch_list = {
            "high_risk": {
                "芯片ETF": {"code": "sh512760", "type": "ETF", "rsi_threshold": 75},
                "科创50": {"code": "sh588000", "type": "ETF", "rsi_threshold": 75},
            },
            "medium_risk": {
                "医药ETF": {"code": "sh512010", "type": "ETF", "rsi_threshold": 70},
            },
            "low_risk": {
                "银行ETF": {"code": "sh512800", "type": "ETF", "rsi_threshold": 65},
            }
        }
        
        # 信号阈值配置
        self.thresholds = {
            "rsi_overbought": 75,      # RSI超买阈值
            "rsi_oversold": 30,        # RSI超卖阈值
            "volume_surge": 1.5,       # 成交量放大倍数
            "change_threshold": 3.0,   # 涨跌幅关注阈值
        }
        
        # 历史数据缓存（用于计算技术指标）
        self.price_history = {}
        
        # 已发送信号记录（避免重复提醒）
        self.sent_signals = set()
        
        # 初始化通知器
        self.notifier = None
        if NOTIFICATION_AVAILABLE:
            try:
                # 尝试从配置文件加载
                self.notifier = create_notifier_from_config('notification_config.json')
                
                # 如果配置文件中没有启用飞书，但设置了环境变量，则手动添加
                import os
                feishu_webhook = os.getenv('FEISHU_WEBHOOK')
                if feishu_webhook and self.notifier:
                    feishu = FeishuNotification(feishu_webhook)
                    self.notifier.add_channel(feishu)
                    logger.info("✅ 已从环境变量加载飞书通知")
                    
            except Exception as e:
                logger.warning(f"初始化通知器失败: {e}")
        
    def fetch_realtime_data(self, symbols: List[str]) -> Dict:
        """从腾讯API获取实时数据"""
        url = f"http://qt.gtimg.cn/q={','.join(symbols)}"
        
        try:
            response = requests.get(url, timeout=10)
            response.encoding = 'gbk'
            
            data = {}
            lines = response.text.strip().split(';')
            
            for line in lines:
                if not line.strip():
                    continue
                
                if 'v_' in line:
                    parts = line.split('~')
                    if len(parts) >= 45:
                        code = parts[2]
                        name = parts[1]
                        price = float(parts[3])
                        prev_close = float(parts[4])
                        open_price = float(parts[5])
                        high = float(parts[33])
                        low = float(parts[34])
                        volume = float(parts[36]) if len(parts) > 36 else 0
                        change_pct = float(parts[32]) if len(parts) > 32 else 0
                        
                        data[code] = {
                            'name': name,
                            'price': price,
                            'prev_close': prev_close,
                            'open': open_price,
                            'high': high,
                            'low': low,
                            'volume': volume,
                            'change_pct': change_pct,
                            'timestamp': datetime.now()
                        }
            
            return data
        except Exception as e:
            logger.error(f"获取数据失败: {e}")
            return {}
    
    def calculate_rsi(self, prices: List[float], period: int = 14) -> float:
        """计算RSI指标"""
        if len(prices) < period + 1:
            return 50.0
        
        gains = []
        losses = []
        
        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        
        # 使用最近period天
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            return 100.0
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi
    
    def calculate_ma(self, prices: List[float], period: int) -> float:
        """计算移动平均线"""
        if len(prices) < period:
            return prices[-1] if prices else 0
        return sum(prices[-period:]) / period
    
    def detect_signals(self, code: str, data: Dict) -> List[Dict]:
        """检测买卖信号"""
        signals = []
        
        # 更新价格历史
        if code not in self.price_history:
            self.price_history[code] = []
        self.price_history[code].append(data['price'])
        
        # 保持最近60天数据
        if len(self.price_history[code]) > 60:
            self.price_history[code] = self.price_history[code][-60:]
        
        prices = self.price_history[code]
        if len(prices) < 20:
            return signals
        
        # 计算技术指标
        rsi = self.calculate_rsi(prices)
        ma5 = self.calculate_ma(prices, 5)
        ma10 = self.calculate_ma(prices, 10)
        ma20 = self.calculate_ma(prices, 20)
        
        current_price = data['price']
        change_pct = data['change_pct']
        
        # 生成信号ID（用于去重）
        today = datetime.now().strftime('%Y%m%d')
        
        # 信号1: RSI超买
        if rsi > self.thresholds['rsi_overbought']:
            signal_id = f"{code}_{today}_rsi_overbought"
            if signal_id not in self.sent_signals:
                signals.append({
                    'type': 'warning',
                    'level': 'high',
                    'title': f"⚠️ {data['name']} RSI超买",
                    'message': f"RSI={rsi:.1f}，超过{self.thresholds['rsi_overbought']}，警惕回调风险",
                    'suggestion': '考虑减仓',
                    'signal_id': signal_id
                })
        
        # 信号2: RSI超卖
        if rsi < self.thresholds['rsi_oversold']:
            signal_id = f"{code}_{today}_rsi_oversold"
            if signal_id not in self.sent_signals:
                signals.append({
                    'type': 'opportunity',
                    'level': 'medium',
                    'title': f"✅ {data['name']} RSI超卖",
                    'message': f"RSI={rsi:.1f}，低于{self.thresholds['rsi_oversold']}，可能存在反弹机会",
                    'suggestion': '关注买入机会',
                    'signal_id': signal_id
                })
        
        # 信号3: 均线死叉 (M5下穿M10)
        if len(prices) >= 10:
            prev_ma5 = self.calculate_ma(prices[:-1], 5)
            prev_ma10 = self.calculate_ma(prices[:-1], 10)
            
            if prev_ma5 > prev_ma10 and ma5 < ma10:
                signal_id = f"{code}_{today}_death_cross"
                if signal_id not in self.sent_signals:
                    signals.append({
                        'type': 'warning',
                        'level': 'high',
                        'title': f"🔴 {data['name']} 均线死叉",
                        'message': f"M5下穿M10，短期趋势转弱",
                        'suggestion': '减仓或观望',
                        'signal_id': signal_id
                    })
        
        # 信号4: 均线金叉 (M5上穿M10)
        if len(prices) >= 10:
            prev_ma5 = self.calculate_ma(prices[:-1], 5)
            prev_ma10 = self.calculate_ma(prices[:-1], 10)
            
            if prev_ma5 < prev_ma10 and ma5 > ma10:
                signal_id = f"{code}_{today}_golden_cross"
                if signal_id not in self.sent_signals:
                    signals.append({
                        'type': 'opportunity',
                        'level': 'medium',
                        'title': f"🟢 {data['name']} 均线金叉",
                        'message': f"M5上穿M10，短期趋势转强",
                        'suggestion': '关注加仓机会',
                        'signal_id': signal_id
                    })
        
        # 信号5: 大涨提醒
        if change_pct > self.thresholds['change_threshold']:
            signal_id = f"{code}_{today}_surge"
            if signal_id not in self.sent_signals:
                signals.append({
                    'type': 'info',
                    'level': 'low',
                    'title': f"📈 {data['name']} 大涨",
                    'message': f"涨幅{change_pct:+.2f}%，突破涨跌幅阈值",
                    'suggestion': '观察持续性',
                    'signal_id': signal_id
                })
        
        # 信号6: 大跌提醒
        if change_pct < -self.thresholds['change_threshold']:
            signal_id = f"{code}_{today}_drop"
            if signal_id not in self.sent_signals:
                signals.append({
                    'type': 'warning',
                    'level': 'medium',
                    'title': f"📉 {data['name']} 大跌",
                    'message': f"跌幅{change_pct:+.2f}%，注意风险",
                    'suggestion': '评估是否止损',
                    'signal_id': signal_id
                })
        
        return signals
    
    def check_sector_rotation(self, all_data: Dict) -> List[Dict]:
        """检测板块轮动信号"""
        rotation_signals = []
        today = datetime.now().strftime('%Y%m%d')
        
        # 获取各板块涨跌幅
        high_risk_change = []
        medium_risk_change = []
        low_risk_change = []
        
        for risk_level, sectors in self.watch_list.items():
            for name, config in sectors.items():
                code = config['code']
                if code in all_data:
                    change = all_data[code]['change_pct']
                    if risk_level == 'high_risk':
                        high_risk_change.append(change)
                    elif risk_level == 'medium_risk':
                        medium_risk_change.append(change)
                    else:
                        low_risk_change.append(change)
        
        # 计算平均涨跌幅
        avg_high = sum(high_risk_change) / len(high_risk_change) if high_risk_change else 0
        avg_medium = sum(medium_risk_change) / len(medium_risk_change) if medium_risk_change else 0
        avg_low = sum(low_risk_change) / len(low_risk_change) if low_risk_change else 0
        
        # 轮动信号1: 高风险→低风险轮动
        if avg_high < -2 and avg_low > 1:
            signal_id = f"rotation_{today}_high_to_low"
            if signal_id not in self.sent_signals:
                rotation_signals.append({
                    'type': 'rotation',
                    'level': 'high',
                    'title': "🔄 板块轮动信号：高风险→低风险",
                    'message': f"高风险板块平均{avg_high:+.2f}%，低风险板块平均{avg_low:+.2f}%",
                    'suggestion': '考虑减仓高风险，加仓低风险',
                    'signal_id': signal_id
                })
        
        # 轮动信号2: 低风险→高风险轮动
        if avg_low < -1 and avg_high > 2:
            signal_id = f"rotation_{today}_low_to_high"
            if signal_id not in self.sent_signals:
                rotation_signals.append({
                    'type': 'rotation',
                    'level': 'medium',
                    'title': "🔄 板块轮动信号：低风险→高风险",
                    'message': f"低风险板块平均{avg_low:+.2f}%，高风险板块平均{avg_high:+.2f}%",
                    'suggestion': '关注高风险板块机会',
                    'signal_id': signal_id
                })
        
        return rotation_signals
    
    def send_notification(self, signals: List[Dict]):
        """发送通知（支持控制台、飞书、微信、钉钉、邮件）"""
        if not signals:
            return
        
        # 1. 控制台输出
        print("\n" + "=" * 60)
        print(f"【板块轮动监控提醒】{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        for signal in signals:
            print(f"\n{signal['title']}")
            print(f"  级别: {'🔴' * (4-signal['level'].count('l'))} {signal['level'].upper()}")
            print(f"  详情: {signal['message']}")
            print(f"  建议: {signal['suggestion']}")
            print("-" * 60)
            
            # 记录已发送信号
            self.sent_signals.add(signal['signal_id'])
            
            # 记录日志
            logger.info(f"信号触发: {signal['title']} - {signal['message']}")
        
        print("\n")
        
        # 2. 发送飞书/微信/钉钉/邮件通知
        if self.notifier and NOTIFICATION_AVAILABLE:
            try:
                title = f"板块轮动监控 - 发现{len(signals)}个信号"
                message = self.notifier.format_signal_message(signals)
                self.notifier.send_all(title, message)
                logger.info(f"已发送多渠道通知: {len(signals)}个信号")
            except Exception as e:
                logger.error(f"发送通知失败: {e}")
    
    def run_once(self):
        """执行一次监控"""
        # 收集所有监控标的代码
        all_codes = []
        for risk_level, sectors in self.watch_list.items():
            for name, config in sectors.items():
                all_codes.append(config['code'])
        
        # 获取实时数据
        logger.info(f"开始获取{len(all_codes)}个标的的实时数据...")
        data = self.fetch_realtime_data(all_codes)
        
        if not data:
            logger.error("获取数据失败")
            return
        
        logger.info(f"成功获取{len(data)}个标的的数据")
        
        # 检测个股信号
        all_signals = []
        for code, info in data.items():
            signals = self.detect_signals(code, info)
            all_signals.extend(signals)
        
        # 检测板块轮动信号
        rotation_signals = self.check_sector_rotation(data)
        all_signals.extend(rotation_signals)
        
        # 发送通知
        if all_signals:
            self.send_notification(all_signals)
        else:
            logger.info("本次监控未发现新信号")
        
        # 保存监控状态
        self.save_state()
    
    def save_state(self):
        """保存监控状态"""
        state = {
            'price_history': {k: v[-30:] for k, v in self.price_history.items()},  # 只保留最近30天
            'sent_signals': list(self.sent_signals)[-100:],  # 只保留最近100个信号
            'last_update': datetime.now().isoformat()
        }
        
        try:
            with open('monitor_state.json', 'w', encoding='utf-8') as f:
                json.dump(state, f, ensure_ascii=False, indent=2)
            logger.info("监控状态已保存")
        except Exception as e:
            logger.error(f"保存状态失败: {e}")
    
    def load_state(self):
        """加载监控状态"""
        try:
            with open('monitor_state.json', 'r', encoding='utf-8') as f:
                state = json.load(f)
                self.price_history = state.get('price_history', {})
                self.sent_signals = set(state.get('sent_signals', []))
                logger.info(f"已加载历史状态，包含{len(self.price_history)}个标的的价格历史")
        except FileNotFoundError:
            logger.info("未找到历史状态，将创建新的监控")
        except Exception as e:
            logger.error(f"加载状态失败: {e}")
    
    def run_continuous(self, interval_minutes: int = 30):
        """持续运行监控"""
        logger.info(f"启动板块轮动监控系统，监控间隔: {interval_minutes}分钟")
        
        # 加载历史状态
        self.load_state()
        
        try:
            while True:
                self.run_once()
                logger.info(f"等待{interval_minutes}分钟后进行下一次监控...")
                time.sleep(interval_minutes * 60)
        except KeyboardInterrupt:
            logger.info("监控已停止")
            self.save_state()


if __name__ == "__main__":
    monitor = SectorRotationMonitor()
    
    # 单次运行（用于测试）
    # monitor.run_once()
    
    # 持续运行（每30分钟监控一次）
    monitor.run_continuous(interval_minutes=30)
