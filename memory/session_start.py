#!/usr/bin/env python3
"""
会话启动入口
每次对话开始时运行此脚本,先查看长期记忆

使用方法:
    python session_start.py
    
或者在其他Python代码中:
    from memory.session_start import load_session_context
    context = load_session_context()
"""

import sys
import os

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from wukong_memory import WukongMemory, SessionContext


def load_session_context() -> SessionContext:
    """
    加载会话上下文 - 对话开始时调用
    
    Returns:
        SessionContext: 包含所有长期记忆信息
        
    Example:
        context = load_session_context()
        print(f"这是第 {context.session_count} 次对话")
        print(f"用户偏好: {context.user_preferences}")
    """
    memory = WukongMemory()
    context = memory.read_memory()
    
    # 打印记忆加载信息
    print("\n" + "="*60)
    print("🐵 悟空记忆系统 - 会话启动")
    print("="*60)
    
    if context.session_count == 0:
        print("👋 初次见面! 我会记住我们的每一次对话。")
    else:
        print(f"📊 这是第 {context.session_count} 次对话")
        
    if context.last_session_date:
        print(f"📅 上次对话: {context.last_session_date[:10]}")
    
    if context.user_preferences:
        print(f"\n💡 已了解你的偏好:")
        for key, value in list(context.user_preferences.items())[:3]:
            print(f"   • {key}: {value}")
    
    if context.recent_topics:
        print(f"\n📝 最近聊过的话题:")
        for topic in context.recent_topics[-3:]:
            if topic:
                print(f"   • {topic[:40]}...")
    
    print("="*60 + "\n")
    
    return context


def get_memory_prompt() -> str:
    """
    获取格式化的记忆提示,用于注入到AI提示词中
    
    Returns:
        str: 格式化的记忆信息
    """
    context = load_session_context()
    
    lines = [
        "【悟空长期记忆】",
        f"- 这是第 {context.session_count + 1} 次对话",
    ]
    
    if context.user_preferences:
        lines.append("- 用户偏好:")
        for key, value in context.user_preferences.items():
            lines.append(f"  • {key}: {value}")
    
    if context.key_learnings:
        lines.append("- 需要注意:")
        for learning in context.key_learnings[-3:]:
            lines.append(f"  • {learning}")
    
    return "\n".join(lines)


if __name__ == "__main__":
    """
    直接运行此脚本查看当前记忆状态
    """
    context = load_session_context()
    
    # 可选: 生成记忆提示
    print("\n🎯 记忆提示文本(可用于AI提示词):")
    print("-" * 60)
    print(get_memory_prompt())
    print("-" * 60)
