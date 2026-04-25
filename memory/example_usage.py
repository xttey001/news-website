#!/usr/bin/env python3
"""
悟空记忆系统 - 完整使用示例
展示"先查看长期记忆，再更新"的完整流程
"""

import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from wukong_memory import WukongMemory, read_context, save_session, remember


def example_1_basic_flow():
    """
    示例1: 基本使用流程
    
    完整的工作流程:
    1. 会话开始 -> read_memory() 读取记忆
    2. 处理任务 -> 使用记忆上下文
    3. 会话结束 -> update_memory() 保存新记忆
    """
    print("="*60)
    print("示例1: 基本使用流程")
    print("="*60)
    
    # ===== 步骤1: 会话开始 - 先查看记忆 =====
    print("\n🟢 步骤1: 会话开始 - 读取长期记忆\n")
    
    memory = WukongMemory()
    context = memory.read_memory()
    
    # 使用记忆上下文
    if context.session_count > 0:
        print(f"欢迎回来! 这是我们第 {context.session_count + 1} 次对话")
    else:
        print("初次见面! 我会记住我们的每一次交流")
    
    # ===== 步骤2: 模拟处理用户请求 =====
    print("\n🟡 步骤2: 处理用户请求\n")
    
    # 模拟用户说:"我喜欢简洁的回答"
    user_input = "我喜欢简洁的回答"
    print(f"用户: {user_input}")
    print("AI: 好的,我会记住你喜欢简洁的风格")
    
    # 从对话中提取关键信息
    new_preferences = {"response_style": "简洁"}
    key_points = ["用户偏好简洁的回答风格"]
    topics = ["用户偏好设置"]
    
    # ===== 步骤3: 会话结束 - 再更新记忆 =====
    print("\n🔵 步骤3: 会话结束 - 更新长期记忆\n")
    
    memory.update_memory({
        "session_summary": "用户设定了回答风格偏好",
        "new_preferences": new_preferences,
        "key_points": key_points,
        "topics_discussed": topics
    })
    
    print("\n✅ 示例1完成!\n")


def example_2_shortcut_functions():
    """
    示例2: 使用快捷函数
    """
    print("="*60)
    print("示例2: 使用快捷函数")
    print("="*60)
    
    # 快捷读取记忆
    print("\n🟢 快捷读取记忆\n")
    context = read_context()
    print(f"当前会话数: {context.session_count}")
    
    # 模拟对话
    print("\n🟡 模拟对话...\n")
    
    # 快捷保存记忆
    print("🔵 快捷保存记忆\n")
    save_session({
        "session_summary": "使用快捷函数示例",
        "key_points": ["快捷函数很方便"],
        "topics_discussed": ["API使用"]
    })
    
    print("\n✅ 示例2完成!\n")


def example_3_remember_function():
    """
    示例3: 使用 remember() 记录重要事情
    """
    print("="*60)
    print("示例3: 记录重要事情")
    print("="*60)
    
    # 在对话中随时记录重要信息
    print("\n💡 对话中记录重要信息:\n")
    
    remember("用户正在开发一个股票分析系统", importance=5)
    remember("用户偏好Python语言", importance=3)
    remember("用户对性能优化很关注", importance=4)
    
    # 查看记忆摘要
    print("\n📊 当前记忆摘要:\n")
    memory = WukongMemory()
    print(memory.get_memory_summary())
    
    print("\n✅ 示例3完成!\n")


def example_4_full_conversation_simulation():
    """
    示例4: 模拟完整对话场景
    """
    print("="*60)
    print("示例4: 完整对话场景模拟")
    print("="*60)
    
    def simulate_conversation(user_messages: list):
        """模拟多轮对话"""
        
        # 1. 读取记忆
        print("\n" + "─"*60)
        print("🐵 悟空: 让我看看我们的对话历史...")
        context = read_context()
        print(f"📝 已加载 {context.session_count} 次历史对话")
        
        if context.user_preferences:
            print(f"💡 已知偏好: {context.user_preferences}")
        print("─"*60)
        
        # 2. 处理对话
        key_points = []
        topics = []
        
        for msg in user_messages:
            print(f"\n👤 用户: {msg}")
            
            # 模拟AI理解和提取关键信息
            if "喜欢" in msg or "偏好" in msg:
                key_points.append(f"用户偏好: {msg}")
            if "项目" in msg or "开发" in msg:
                topics.append("项目开发")
            
            print(f"🤖 悟空: 收到! (已理解意图)")
        
        # 3. 保存记忆
        print("\n" + "─"*60)
        print("🐵 悟空: 正在保存这次对话的记忆...")
        save_session({
            "session_summary": f"进行了{len(user_messages)}轮对话",
            "key_points": key_points,
            "topics_discussed": topics
        })
        print("─"*60)
    
    # 模拟多轮对话
    conversation = [
        "你好,我想做一个数据分析工具",
        "我偏好使用Python",
        "希望界面简洁一些",
        "性能很重要,数据量可能很大"
    ]
    
    simulate_conversation(conversation)
    
    print("\n✅ 示例4完成!\n")


def example_5_memory_in_prompt():
    """
    示例5: 将记忆注入到AI提示词中
    """
    print("="*60)
    print("示例5: 记忆注入提示词")
    print("="*60)
    
    from session_start import get_memory_prompt
    
    # 获取格式化的记忆提示
    memory_prompt = get_memory_prompt()
    
    # 构建完整提示词
    full_prompt = f"""
{memory_prompt}

【当前任务】
请帮我优化数据库查询性能

请根据以上记忆,用用户偏好的风格回答问题。
"""
    
    print("\n📝 完整提示词:\n")
    print(full_prompt)
    
    print("\n✅ 示例5完成!\n")


def show_memory_status():
    """显示当前记忆状态"""
    print("="*60)
    print("🧠 当前记忆状态")
    print("="*60)
    
    memory = WukongMemory()
    print(memory.get_memory_summary())


if __name__ == "__main__":
    """
    运行所有示例
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="悟空记忆系统使用示例")
    parser.add_argument(
        "--example", "-e",
        type=int,
        choices=[1, 2, 3, 4, 5],
        help="运行指定示例 (1-5)"
    )
    parser.add_argument(
        "--status", "-s",
        action="store_true",
        help="显示记忆状态"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="运行所有示例"
    )
    
    args = parser.parse_args()
    
    if args.status:
        show_memory_status()
    elif args.example == 1:
        example_1_basic_flow()
    elif args.example == 2:
        example_2_shortcut_functions()
    elif args.example == 3:
        example_3_remember_function()
    elif args.example == 4:
        example_4_full_conversation_simulation()
    elif args.example == 5:
        example_5_memory_in_prompt()
    else:
        # 默认运行所有示例
        print("\n🚀 运行所有示例...\n")
        example_1_basic_flow()
        example_2_shortcut_functions()
        example_3_remember_function()
        example_4_full_conversation_simulation()
        example_5_memory_in_prompt()
        show_memory_status()
