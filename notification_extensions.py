#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通知扩展模块
支持微信、钉钉、邮件等多种通知方式
"""

import json
import requests
from typing import Dict, List
from datetime import datetime


class NotificationSender:
    """通知发送器基类"""
    
    def send(self, title: str, message: str) -> bool:
        """发送通知，子类需要实现"""
        raise NotImplementedError


class WechatWorkNotification(NotificationSender):
    """企业微信通知"""
    
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
    
    def send(self, title: str, message: str) -> bool:
        """发送企业微信消息"""
        try:
            data = {
                "msgtype": "markdown",
                "markdown": {
                    "content": f"**{title}**\n\n{message}"
                }
            }
            
            response = requests.post(
                self.webhook_url,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get('errcode') == 0:
                    print(f"✅ 企业微信通知发送成功: {title}")
                    return True
            
            print(f"❌ 企业微信通知发送失败: {response.text}")
            return False
            
        except Exception as e:
            print(f"❌ 企业微信通知异常: {e}")
            return False


class DingTalkNotification(NotificationSender):
    """钉钉通知"""
    
    def __init__(self, webhook_url: str, secret: str = None):
        self.webhook_url = webhook_url
        self.secret = secret
    
    def send(self, title: str, message: str) -> bool:
        """发送钉钉消息"""
        try:
            data = {
                "msgtype": "markdown",
                "markdown": {
                    "title": title,
                    "text": f"### {title}\n\n{message}"
                }
            }
            
            response = requests.post(
                self.webhook_url,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get('errcode') == 0:
                    print(f"✅ 钉钉通知发送成功: {title}")
                    return True
            
            print(f"❌ 钉钉通知发送失败: {response.text}")
            return False
            
        except Exception as e:
            print(f"❌ 钉钉通知异常: {e}")
            return False


class EmailNotification(NotificationSender):
    """邮件通知"""
    
    def __init__(self, smtp_server: str, smtp_port: int, sender: str, password: str, receiver: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender = sender
        self.password = password
        self.receiver = receiver
    
    def send(self, title: str, message: str) -> bool:
        """发送邮件"""
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            
            msg = MIMEMultipart()
            msg['From'] = self.sender
            msg['To'] = self.receiver
            msg['Subject'] = title
            
            # 将markdown格式转换为HTML
            html_content = message.replace('\n', '<br>')
            html_content = html_content.replace('**', '<b>').replace('**', '</b>')
            
            msg.attach(MIMEText(html_content, 'html', 'utf-8'))
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender, self.password)
            server.send_message(msg)
            server.quit()
            
            print(f"✅ 邮件通知发送成功: {title}")
            return True
            
        except Exception as e:
            print(f"❌ 邮件通知异常: {e}")
            return False


class MultiChannelNotifier:
    """多渠道通知管理器"""
    
    def __init__(self):
        self.channels: List[NotificationSender] = []
    
    def add_channel(self, channel: NotificationSender):
        """添加通知渠道"""
        self.channels.append(channel)
    
    def send_all(self, title: str, message: str):
        """向所有渠道发送通知"""
        results = []
        for channel in self.channels:
            result = channel.send(title, message)
            results.append(result)
        return all(results)
    
    def format_signal_message(self, signals: List[Dict]) -> str:
        """格式化信号消息"""
        lines = []
        lines.append(f"📊 **板块轮动监控报告**")
        lines.append(f"⏰ 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"📈 发现 **{len(signals)}** 个信号\n")
        
        for i, signal in enumerate(signals, 1):
            level_emoji = {
                'high': '🔴',
                'medium': '🟡',
                'low': '🟢'
            }.get(signal['level'], '⚪')
            
            lines.append(f"{i}. {level_emoji} **{signal['title']}**")
            lines.append(f"   📋 {signal['message']}")
            lines.append(f"   💡 建议: {signal['suggestion']}\n")
        
        lines.append("---")
        lines.append("🤖 自动发送自板块轮动监控系统")
        
        return '\n'.join(lines)


# 配置示例
def create_notifier_from_config(config_file: str = 'notification_config.json') -> MultiChannelNotifier:
    """从配置文件创建通知器"""
    notifier = MultiChannelNotifier()
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 企业微信
        if 'wechat_work' in config and config['wechat_work'].get('enabled'):
            wechat = WechatWorkNotification(config['wechat_work']['webhook_url'])
            notifier.add_channel(wechat)
            print("✅ 已加载企业微信通知")
        
        # 钉钉
        if 'dingtalk' in config and config['dingtalk'].get('enabled'):
            dingtalk = DingTalkNotification(
                config['dingtalk']['webhook_url'],
                config['dingtalk'].get('secret')
            )
            notifier.add_channel(dingtalk)
            print("✅ 已加载钉钉通知")
        
        # 邮件
        if 'email' in config and config['email'].get('enabled'):
            email = EmailNotification(
                config['email']['smtp_server'],
                config['email']['smtp_port'],
                config['email']['sender'],
                config['email']['password'],
                config['email']['receiver']
            )
            notifier.add_channel(email)
            print("✅ 已加载邮件通知")
            
    except FileNotFoundError:
        print(f"⚠️ 配置文件 {config_file} 不存在，使用默认控制台输出")
    except Exception as e:
        print(f"⚠️ 加载配置失败: {e}，使用默认控制台输出")
    
    return notifier


# 配置文件模板
CONFIG_TEMPLATE = {
    "wechat_work": {
        "enabled": False,
        "webhook_url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY"
    },
    "dingtalk": {
        "enabled": False,
        "webhook_url": "https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN",
        "secret": "YOUR_SECRET"
    },
    "email": {
        "enabled": False,
        "smtp_server": "smtp.qq.com",
        "smtp_port": 587,
        "sender": "your_email@qq.com",
        "password": "your_auth_code",
        "receiver": "receiver@example.com"
    }
}


if __name__ == "__main__":
    # 创建配置文件模板
    import os
    
    config_file = 'notification_config.json'
    if not os.path.exists(config_file):
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(CONFIG_TEMPLATE, f, ensure_ascii=False, indent=2)
        print(f"✅ 已创建配置文件模板: {config_file}")
        print("请编辑配置文件，填入您的 webhook URL 或邮箱信息")
    else:
        print(f"配置文件已存在: {config_file}")
    
    # 测试通知
    print("\n测试通知功能...")
    notifier = create_notifier_from_config()
    
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
        }
    ]
    
    message = notifier.format_signal_message(test_signals)
    notifier.send_all("板块轮动监控提醒", message)
