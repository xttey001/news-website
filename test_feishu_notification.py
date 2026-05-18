#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试飞书通知功能
"""

import sys
from notification_extensions import FeishuNotification, MultiChannelNotifier

def test_feishu_notification():
    """测试飞书通知"""
    
    # 飞书 webhook URL（您提供的）
    webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/8baf3f7e-f36e-4bb4-b74d-854e022a3774"
    
    print("=" * 60)
    print("飞书通知测试")
    print("=" * 60)
    print(f"Webhook: {webhook_url[:50]}...")
    print()
    
    # 创建飞书通知器
    feishu = FeishuNotification(webhook_url)
    
    # 测试消息
    title = "🧪 板块轮动监控系统 - 测试消息"
    message = """**系统状态**: 运行正常 ✅

**测试内容**:
1. 飞书 webhook 连接测试
2. 消息格式显示测试
3. 卡片消息渲染测试

**监控标的**:
- 🔴 高风险: 芯片ETF、科创50
- 🟡 中风险: 医药ETF、创业板ETF
- 🟢 低风险: 银行ETF、红利ETF

---
⏰ 测试时间: 2026-05-12
🤖 自动发送自板块轮动监控系统"""
    
    print("正在发送测试消息到飞书...")
    print()
    
    # 发送通知
    result = feishu.send(title, message)
    
    if result:
        print("✅ 测试成功！请检查飞书群是否收到消息")
        return 0
    else:
        print("❌ 测试失败！请检查:")
        print("   1. Webhook URL 是否正确")
        print("   2. 飞书机器人是否被删除或禁用")
        print("   3. 网络连接是否正常")
        return 1

def test_with_monitor_signals():
    """使用真实监控信号格式测试"""
    
    webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/8baf3f7e-f36e-4bb4-b74d-854e022a3774"
    
    print("\n" + "=" * 60)
    print("模拟真实监控信号测试")
    print("=" * 60)
    
    # 创建多渠道通知器
    notifier = MultiChannelNotifier()
    feishu = FeishuNotification(webhook_url)
    notifier.add_channel(feishu)
    
    # 模拟监控信号
    test_signals = [
        {
            'type': 'warning',
            'level': 'high',
            'title': '⚠️ 芯片ETF RSI超买',
            'message': 'RSI=78.5，超过75，警惕回调风险',
            'suggestion': '考虑减仓'
        },
        {
            'type': 'rotation',
            'level': 'medium',
            'title': '🔄 板块轮动信号：高风险→低风险',
            'message': '高风险板块平均-2.5%，低风险板块平均+1.8%',
            'suggestion': '考虑减仓高风险，加仓低风险'
        },
        {
            'type': 'opportunity',
            'level': 'low',
            'title': '🟢 银行ETF 均线金叉',
            'message': 'M5上穿M10，短期趋势转强',
            'suggestion': '关注加仓机会'
        }
    ]
    
    # 格式化消息
    message = notifier.format_signal_message(test_signals)
    title = f"📊 板块轮动监控 - 发现{len(test_signals)}个信号"
    
    print("正在发送模拟监控信号...")
    print()
    
    # 发送通知
    result = notifier.send_all(title, message)
    
    if result:
        print("✅ 模拟信号发送成功！")
        return 0
    else:
        print("❌ 模拟信号发送失败！")
        return 1

if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 15 + "板块轮动监控系统" + " " * 27 + "║")
    print("║" + " " * 18 + "飞书通知测试" + " " * 28 + "║")
    print("╚" + "=" * 58 + "╝")
    print("\n")
    
    # 运行测试1：基础连接测试
    result1 = test_feishu_notification()
    
    # 运行测试2：模拟信号测试
    result2 = test_with_monitor_signals()
    
    # 总结
    print("\n" + "=" * 60)
    print("测试结果总结")
    print("=" * 60)
    print(f"基础连接测试: {'✅ 通过' if result1 == 0 else '❌ 失败'}")
    print(f"模拟信号测试: {'✅ 通过' if result2 == 0 else '❌ 失败'}")
    print()
    
    if result1 == 0 and result2 == 0:
        print("🎉 所有测试通过！飞书通知功能已就绪")
        print()
        print("现在您可以运行监控程序:")
        print("  python sector_rotation_monitor.py")
        print("  或双击: run_sector_monitor.bat")
        sys.exit(0)
    else:
        print("⚠️ 部分测试失败，请检查配置")
        sys.exit(1)
