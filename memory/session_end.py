#!/usr/bin/env python3
"""
会话结束出口
每次对话结束时运行此脚本,更新长期记忆

使用方法:
    python session_end.py --summary "本次对话摘要" --key-points "要点1" "要点2"
    
或者在其他Python代码中:
    from memory.session_end import save_session_summary
    save_session_summary(
        summary="对话摘要",
        key_points=["要点1", "要点2"],
        new_preferences={"theme": "dark"}
    )
"""

import sys
import os
import argparse
from typing import List, Dict, Any, Optional

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from wukong_memory import WukongMemory, save_session


def save_session_summary(
    summary: str,
    key_points: Optional[List[str]] = None,
    topics: Optional[List[str]] = None,
    new_preferences: Optional[Dict[str, Any]] = None,
    important_events: Optional[List[str]] = None
) -> None:
    """
    保存会话摘要 - 对话结束时调用
    
    Args:
        summary: 本次对话的简短摘要
        key_points: 关键要点/学习点
        topics: 讨论的话题列表
        new_preferences: 新发现的用户偏好
        important_events: 重要事件
        
    Example:
        save_session_summary(
            summary="用户询问如何优化数据库性能",
            key_points=["用户使用PostgreSQL", "表数据量约1000万行"],
            topics=["数据库优化", "索引设计"],
            new_preferences={"db": "PostgreSQL"}
        )
    """
    memory = WukongMemory()
    
    # 构建会话数据
    session_data = {
        "session_summary": summary,
        "key_points": key_points or [],
        "topics_discussed": topics or [],
        "new_preferences": new_preferences or {},
        "important_events": important_events or []
    }
    
    # 更新记忆
    memory.update_memory(session_data)
    
    print("\n" + "="*60)
    print("🐵 悟空记忆系统 - 会话结束")
    print("="*60)
    print(f"✅ 已保存会话摘要: {summary[:50]}...")
    
    if key_points:
        print(f"\n📝 关键要点 ({len(key_points)} 条):")
        for point in key_points:
            print(f"   • {point[:50]}...")
    
    if new_preferences:
        print(f"\n💡 更新的偏好:")
        for key, value in new_preferences.items():
            print(f"   • {key}: {value}")
    
    print("="*60 + "\n")


def quick_save(summary: str) -> None:
    """
    快速保存 - 只记录摘要
    
    Args:
        summary: 会话摘要
    """
    save_session_summary(summary=summary)


def interactive_save() -> None:
    """
    交互式保存 - 引导用户输入信息
    """
    print("\n" + "="*60)
    print("🐵 悟空记忆系统 - 保存会话")
    print("="*60)
    
    summary = input("请输入本次对话摘要: ").strip()
    
    key_points = []
    print("\n请输入关键要点 (每行一条,空行结束):")
    while True:
        point = input("  > ").strip()
        if not point:
            break
        key_points.append(point)
    
    topics = []
    print("\n请输入讨论的话题 (每行一个,空行结束):")
    while True:
        topic = input("  > ").strip()
        if not topic:
            break
        topics.append(topic)
    
    # 保存
    save_session_summary(
        summary=summary,
        key_points=key_points,
        topics=topics
    )
    
    print("✅ 会话已保存!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="保存会话到长期记忆")
    parser.add_argument(
        "--summary", "-s",
        type=str,
        help="会话摘要"
    )
    parser.add_argument(
        "--key-points", "-k",
        nargs="+",
        help="关键要点"
    )
    parser.add_argument(
        "--topics", "-t",
        nargs="+",
        help="讨论话题"
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="交互式输入"
    )
    parser.add_argument(
        "--quick", "-q",
        type=str,
        help="快速保存(仅摘要)"
    )
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_save()
    elif args.quick:
        quick_save(args.quick)
    elif args.summary:
        save_session_summary(
            summary=args.summary,
            key_points=args.key_points,
            topics=args.topics
        )
    else:
        # 默认交互式
        interactive_save()
