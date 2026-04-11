# -*- coding: utf-8 -*-
"""
双均线金叉策略回测 - 近5年表现分析
"""

import backtrader as bt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import akshare as ak
import warnings
warnings.filterwarnings('ignore')

# 设置matplotlib中文显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

class DoubleMAStrategy(bt.Strategy):
    """双均线金叉策略"""
    params = (
        ('fast_period', 5),    # 快线周期
        ('slow_period', 20),   # 慢线周期
        ('printlog', True),
    )
    
    def __init__(self):
        # 初始化策略指标
        self.fast_ma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.fast_period)
        self.slow_ma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.slow_period)
        
        # 金叉信号
        self.crossover = bt.indicators.CrossOver(self.fast_ma, self.slow_ma)
        
        # 记录交易
        self.order = None
        self.buy_price = None
        self.buy_comm = None
        
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status in [order.Completed]:
            if order.isbuy():
                if self.params.printlog:
                    print(f'买入执行: 价格={order.executed.price:.2f}, '
                          f'成本={order.executed.value:.2f}, '
                          f'手续费={order.executed.comm:.2f}')
                self.buy_price = order.executed.price
                self.buy_comm = order.executed.comm
            else:
                if self.params.printlog:
                    print(f'卖出执行: 价格={order.executed.price:.2f}, '
                          f'成本={order.executed.value:.2f}, '
                          f'手续费={order.executed.comm:.2f}')
        
        self.order = None
        
    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        
        if self.params.printlog:
            print(f'交易盈亏: 毛利={trade.pnl:.2f}, 净利={trade.pnlcomm:.2f}')
    
    def next(self):
        if self.order:
            return
        
        # 没有持仓
        if not self.position:
            # 金叉信号：快线上穿慢线
            if self.crossover > 0:
                if self.params.printlog:
                    print(f'{self.data.datetime.date()}, 金叉信号, 买入')
                # 全仓买入
                self.order = self.buy()
        # 有持仓
        else:
            # 死叉信号：快线下穿慢线
            if self.crossover < 0:
                if self.params.printlog:
                    print(f'{self.data.datetime.date()}, 死叉信号, 卖出')
                # 全部卖出
                self.order = self.sell()
    
    def stop(self):
        if self.params.printlog:
            print(f'策略结束，快线周期={self.params.fast_period}, '
                  f'慢线周期={self.params.slow_period}')
                  # f'期末价值={self.broker.getvalue():.2f}')

def get_stock_data(symbol='000300', start_date='2020-01-01', end_date='2025-01-01'):
    """获取股票数据"""
    try:
        print(f'正在获取 {symbol} 数据...')
        
        # 使用akshare获取沪深300指数数据
        if symbol == '000300':
            df = ak.stock_zh_index_daily(symbol="sh000300")
            df['date'] = pd.to_datetime(df['date'])
            df = df.set_index('date')
            df = df.sort_index()
            
            # 筛选日期范围
            df = df[(df.index >= start_date) & (df.index <= end_date)]
            
            # 重命名列以符合backtrader要求
            df = df[['open', 'high', 'low', 'close', 'volume']]
            
        print(f'成功获取数据，共 {len(df)} 个交易日')
        return df
        
    except Exception as e:
        print(f'获取数据失败: {e}')
        return None

def run_backtest():
    """运行回测"""
    print('='*60)
    print('双均线金叉策略回测 - 近5年表现')
    print('='*60)
    
    # 创建回测引擎
    cerebro = bt.Cerebro()
    
    # 设置初始资金
    cerebro.broker.setcash(100000.0)
    
    # 设置手续费
    cerebro.broker.setcommission(commission=0.001)  # 0.1%
    
    # 获取数据
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')
    
    df = get_stock_data(symbol='000300', start_date=start_date, end_date=end_date)
    
    if df is None or len(df) == 0:
        print('无法获取数据，请检查网络连接')
        return
    
    # 将数据添加到回测引擎
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    
    # 添加策略
    cerebro.addstrategy(DoubleMAStrategy, fast_period=5, slow_period=20)
    
    # 添加分析指标
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe', riskfreerate=0.03)
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
    
    # 运行回测
    print(f'\n初始资金: {cerebro.broker.getvalue():.2f}')
    print('开始回测...\n')
    
    results = cerebro.run()
    strat = results[0]
    
    # 获取分析结果
    final_value = cerebro.broker.getvalue()
    sharpe = strat.analyzers.sharpe.get_analysis()
    drawdown = strat.analyzers.drawdown.get_analysis()
    returns = strat.analyzers.returns.get_analysis()
    trades = strat.analyzers.trades.get_analysis()
    
    # 计算绩效指标
    total_return = (final_value - 100000) / 100000 * 100
    annual_return = total_return / 5  # 简单年化
    max_drawdown = drawdown.get('max', {}).get('drawdown', 0)
    sharpe_ratio = sharpe.get('sharperatio', 0)
    
    total_trades = trades.get('total', {}).get('total', 0)
    won_trades = trades.get('won', {}).get('total', 0)
    lost_trades = trades.get('lost', {}).get('total', 0)
    win_rate = (won_trades / total_trades * 100) if total_trades > 0 else 0
    
    # 打印回测报告
    print('\n' + '='*60)
    print('[量化策略回测报告]')
    print('='*60)
    print(f'\n生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    
    print('\n## 核心发现')
    print(f'1. 策略总收益: {total_return:.2f}%，年化收益约 {annual_return:.2f}%')
    print(f'2. 最大回撤: {max_drawdown:.2f}%，风险控制{"良好" if max_drawdown < 20 else "需改进"}')
    print(f'3. 夏普比率: {sharpe_ratio:.2f}，{"优秀" if sharpe_ratio > 1 else "一般" if sharpe_ratio > 0.5 else "较差"}')
    
    print('\n## 绩效指标')
    print('| 指标 | 数值 | 评级 |')
    print('|------|------|------|')
    print(f'| 期末资金 | {final_value:,.2f}元 | - |')
    print(f'| 总收益率 | {total_return:.2f}% | {"[优秀]" if total_return > 50 else "[良好]" if total_return > 20 else "[一般]"} |')
    print(f'| 年化收益 | {annual_return:.2f}% | {"[良好]" if annual_return > 10 else "[一般]"} |')
    print(f'| 最大回撤 | {max_drawdown:.2f}% | {"[优秀]" if max_drawdown < 10 else "[良好]" if max_drawdown < 20 else "[需改进]"} |')
    print(f'| 夏普比率 | {sharpe_ratio:.2f} | {"[优秀]" if sharpe_ratio > 2 else "[良好]" if sharpe_ratio > 1 else "[一般]"} |')
    print(f'| 交易次数 | {total_trades}次 | - |')
    print(f'| 胜率 | {win_rate:.2f}% | {"[优秀]" if win_rate > 60 else "[良好]" if win_rate > 50 else "[需改进]"} |')
    
    print('\n## 交易统计')
    print(f'- 总交易次数: {total_trades} 次')
    print(f'- 盈利交易: {won_trades} 次')
    print(f'- 亏损交易: {lost_trades} 次')
    print(f'- 胜率: {win_rate:.2f}%')
    
    if total_trades > 0:
        avg_profit = trades.get('won', {}).get('pnl', {}).get('average', 0)
        avg_loss = trades.get('lost', {}).get('pnl', {}).get('average', 0)
        print(f'- 平均盈利: {avg_profit:.2f}元')
        print(f'- 平均亏损: {avg_loss:.2f}元')
        if avg_loss != 0:
            profit_loss_ratio = abs(avg_profit / avg_loss)
            print(f'- 盈亏比: {profit_loss_ratio:.2f}')
    
    print('\n## 策略参数')
    print('- 快线周期: 5日均线')
    print('- 慢线周期: 20日均线')
    print('- 标的: 沪深300指数 (000300)')
    print(f'- 回测周期: {start_date} 至 {end_date}')
    print('- 初始资金: 100,000元')
    print('- 手续费: 0.1%')
    
    print('\n## 行动建议')
    print('| 优先级 | 建议 | 预期效果 |')
    print('|--------|------|----------|')
    
    if sharpe_ratio < 1:
        print('| [高] | 优化均线参数组合，尝试更长周期 | 提高夏普比率至1.0以上 |')
    if max_drawdown > 20:
        print('| [高] | 添加止损机制，控制单笔亏损 | 降低最大回撤至15%以内 |')
    if win_rate < 50:
        print('| [中] | 增加趋势过滤条件，减少假信号 | 提高胜率至55%以上 |')
    if total_return < 20:
        print('| [中] | 考虑加入仓位管理策略 | 提升收益率至30%以上 |')
    else:
        print('| 🟢 低 | 保持当前策略，定期复盘 | 维持稳定收益 |')
    
    print('\n## 风险提示')
    print('- 历史回测不代表未来表现')
    print('- 交易成本和滑点可能影响实际收益')
    print('- 建议在模拟盘验证后再实盘操作')
    
    # 绘制回测结果图
    try:
        print('\n正在生成回测图表...')
        
        # 创建图表
        fig, axes = plt.subplots(2, 1, figsize=(14, 10))
        
        # 价格和均线图
        ax1 = axes[0]
        df_plot = df.copy()
        df_plot['MA5'] = df_plot['close'].rolling(window=5).mean()
        df_plot['MA20'] = df_plot['close'].rolling(window=20).mean()
        
        ax1.plot(df_plot.index, df_plot['close'], label='沪深300', linewidth=1.5, alpha=0.8)
        ax1.plot(df_plot.index, df_plot['MA5'], label='MA5', linewidth=1, alpha=0.7)
        ax1.plot(df_plot.index, df_plot['MA20'], label='MA20', linewidth=1, alpha=0.7)
        
        ax1.set_title('沪深300指数 - 双均线金叉策略', fontsize=14, fontweight='bold')
        ax1.set_xlabel('日期')
        ax1.set_ylabel('价格')
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # 资金曲线图（简化版）
        ax2 = axes[1]
        # 使用买入持有策略对比
        buy_hold_return = (df['close'][-1] - df['close'][0]) / df['close'][0] * 100
        ax2.text(0.5, 0.7, f'策略总收益: {total_return:.2f}%', 
                transform=ax2.transAxes, fontsize=16, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
        ax2.text(0.5, 0.5, f'买入持有收益: {buy_hold_return:.2f}%', 
                transform=ax2.transAxes, fontsize=16, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
        ax2.text(0.5, 0.3, f'策略超额收益: {total_return - buy_hold_return:.2f}%', 
                transform=ax2.transAxes, fontsize=16, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
        
        ax2.set_title('策略收益对比', fontsize=14, fontweight='bold')
        ax2.axis('off')
        
        plt.tight_layout()
        
        # 保存图表
        chart_path = 'C:/Users/asus/.qclaw/workspace/quant_backtest_result.png'
        plt.savefig(chart_path, dpi=150, bbox_inches='tight')
        print(f'图表已保存: {chart_path}')
        
        plt.close()
        
    except Exception as e:
        print(f'生成图表时出错: {e}')
    
    print('\n回测完成！')
    return {
        'total_return': total_return,
        'annual_return': annual_return,
        'max_drawdown': max_drawdown,
        'sharpe_ratio': sharpe_ratio,
        'win_rate': win_rate,
        'total_trades': total_trades
    }

if __name__ == '__main__':
    run_backtest()
