"""
悟空记忆管理系统
实现"先查看长期记忆，再更新"的机制
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict


@dataclass
class MemoryEntry:
    """记忆条目"""
    timestamp: str
    category: str  # preference, event, lesson, context
    content: Dict[str, Any]
    importance: int = 1  # 1-5, 5最重要
    
    def to_dict(self) -> Dict:
        return {
            "timestamp": self.timestamp,
            "category": self.category,
            "content": self.content,
            "importance": self.importance
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "MemoryEntry":
        return cls(
            timestamp=data["timestamp"],
            category=data["category"],
            content=data["content"],
            importance=data.get("importance", 1)
        )


@dataclass
class SessionContext:
    """会话上下文"""
    user_preferences: Dict[str, Any] = field(default_factory=dict)
    recent_topics: List[str] = field(default_factory=list)
    key_learnings: List[str] = field(default_factory=list)
    session_count: int = 0
    last_session_date: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return asdict(self)


class WukongMemory:
    """
    悟空长期记忆系统
    
    核心机制:
    1. 会话开始时: read_memory() - 读取所有相关记忆
    2. 会话进行中: 使用记忆上下文处理任务
    3. 会话结束时: update_memory() - 保存新的记忆
    
    使用示例:
        memory = WukongMemory()
        
        # 会话开始 - 先读取记忆
        context = memory.read_memory()
        
        # ... 处理用户请求 ...
        
        # 会话结束 - 再更新记忆
        memory.update_memory({
            "new_preferences": {"theme": "dark"},
            "key_points": ["用户喜欢简洁的回答"]
        })
    """
    
    def __init__(self, workspace_path: str = None):
        """
        初始化记忆系统
        
        Args:
            workspace_path: 工作空间路径,默认使用当前workspace
        """
        if workspace_path is None:
            workspace_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        self.workspace_path = Path(workspace_path)
        self.memory_dir = self.workspace_path / "memory"
        self.memory_file = self.memory_dir / "wukong_long_term_memory.json"
        
        # 确保目录存在
        self.memory_dir.mkdir(exist_ok=True)
        
        # 加载或初始化记忆
        self._memory_data = self._load_memory()
    
    def _load_memory(self) -> Dict:
        """加载长期记忆文件"""
        if self.memory_file.exists():
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"⚠️ 读取记忆文件失败: {e}, 创建新记忆")
        
        return {
            "version": "1.0",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "session_count": 0,
            "user_profile": {
                "preferences": {},
                "communication_style": {},
                "interests": [],
                "avoid_topics": []
            },
            "conversation_history": [],
            "key_memories": [],  # 重要记忆条目
            "session_summaries": []  # 会话摘要
        }
    
    def _save_memory(self) -> None:
        """保存记忆到文件"""
        self._memory_data["updated_at"] = datetime.now().isoformat()
        
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self._memory_data, f, ensure_ascii=False, indent=2)
    
    def read_memory(self) -> SessionContext:
        """
        查看长期记忆 - 每次会话开始时调用
        
        Returns:
            SessionContext: 包含所有相关记忆上下文
        """
        print("🐵 悟空正在读取长期记忆...")
        
        context = SessionContext()
        
        # 1. 加载用户偏好
        user_profile = self._memory_data.get("user_profile", {})
        context.user_preferences = user_profile.get("preferences", {})
        
        # 2. 获取最近的话题
        history = self._memory_data.get("conversation_history", [])
        recent = history[-5:] if len(history) > 5 else history
        context.recent_topics = [
            h.get("summary", "") for h in recent
        ]
        
        # 3. 获取关键学习点
        key_memories = self._memory_data.get("key_memories", [])
        important_memories = [m for m in key_memories if m.get("importance", 1) >= 3]
        context.key_learnings = [
            m.get("content", {}).get("description", "") 
            for m in important_memories[-10:]
        ]
        
        # 4. 会话统计
        context.session_count = self._memory_data.get("session_count", 0)
        summaries = self._memory_data.get("session_summaries", [])
        if summaries:
            context.last_session_date = summaries[-1].get("date")
        
        print(f"✅ 记忆加载完成:")
        print(f"   - 已进行会话: {context.session_count} 次")
        print(f"   - 用户偏好: {len(context.user_preferences)} 项")
        print(f"   - 最近话题: {len(context.recent_topics)} 个")
        print(f"   - 关键记忆: {len(context.key_learnings)} 条")
        
        return context
    
    def update_memory(self, session_data: Dict[str, Any]) -> None:
        """
        更新长期记忆 - 每次会话结束时调用
        
        Args:
            session_data: 会话数据,包含:
                - session_summary: 会话摘要
                - new_preferences: 新发现的用户偏好
                - key_points: 关键要点/学习点
                - topics_discussed: 讨论的话题列表
                - importance_events: 重要事件
        """
        print("🐵 悟空正在更新长期记忆...")
        
        now = datetime.now()
        
        # 1. 更新会话计数
        self._memory_data["session_count"] = self._memory_data.get("session_count", 0) + 1
        
        # 2. 添加会话摘要
        session_summary = {
            "date": now.isoformat(),
            "summary": session_data.get("session_summary", ""),
            "topics": session_data.get("topics_discussed", []),
            "key_points": session_data.get("key_points", [])
        }
        self._memory_data["session_summaries"].append(session_summary)
        
        # 限制历史数量(保留最近50次)
        if len(self._memory_data["session_summaries"]) > 50:
            self._memory_data["session_summaries"] = self._memory_data["session_summaries"][-50:]
        
        # 3. 更新用户偏好
        new_prefs = session_data.get("new_preferences", {})
        if new_prefs:
            self._memory_data["user_profile"]["preferences"].update(new_prefs)
            print(f"   📝 更新偏好: {list(new_prefs.keys())}")
        
        # 4. 添加关键记忆
        for point in session_data.get("key_points", []):
            memory_entry = MemoryEntry(
                timestamp=now.isoformat(),
                category="lesson",
                content={"description": point},
                importance=3
            )
            self._memory_data["key_memories"].append(memory_entry.to_dict())
        
        # 限制关键记忆数量
        if len(self._memory_data["key_memories"]) > 100:
            # 按重要性排序,保留重要的
            memories = self._memory_data["key_memories"]
            memories.sort(key=lambda x: x.get("importance", 1), reverse=True)
            self._memory_data["key_memories"] = memories[:100]
        
        # 5. 保存到文件
        self._save_memory()
        
        print(f"✅ 记忆更新完成:")
        print(f"   - 总会话数: {self._memory_data['session_count']}")
        print(f"   - 关键记忆: {len(self._memory_data['key_memories'])} 条")
    
    def add_important_memory(self, description: str, category: str = "event", importance: int = 4) -> None:
        """
        添加重要记忆
        
        Args:
            description: 记忆描述
            category: 记忆类别 (preference, event, lesson, context)
            importance: 重要程度 1-5
        """
        entry = MemoryEntry(
            timestamp=datetime.now().isoformat(),
            category=category,
            content={"description": description},
            importance=importance
        )
        
        self._memory_data["key_memories"].append(entry.to_dict())
        self._save_memory()
        
        print(f"💾 已保存重要记忆: {description[:50]}...")
    
    def get_memory_summary(self) -> str:
        """获取记忆摘要报告"""
        lines = [
            "=" * 50,
            "🧠 悟空长期记忆摘要",
            "=" * 50,
            f"总会话次数: {self._memory_data.get('session_count', 0)}",
            f"关键记忆数: {len(self._memory_data.get('key_memories', []))}",
            f"最后更新: {self._memory_data.get('updated_at', 'N/A')}",
            "",
            "📌 用户偏好:",
        ]
        
        prefs = self._memory_data.get("user_profile", {}).get("preferences", {})
        for key, value in prefs.items():
            lines.append(f"  - {key}: {value}")
        
        lines.extend(["", "🔑 最近关键记忆:"])
        memories = self._memory_data.get("key_memories", [])[-5:]
        for mem in memories:
            desc = mem.get("content", {}).get("description", "")[:40]
            lines.append(f"  - {desc}...")
        
        lines.append("=" * 50)
        
        return "\n".join(lines)
    
    def clear_memory(self, confirm: bool = False) -> None:
        """
        清空所有记忆 (谨慎使用!)
        
        Args:
            confirm: 必须传入 True 确认清空
        """
        if not confirm:
            print("⚠️ 请传入 confirm=True 确认清空记忆")
            return
        
        if self.memory_file.exists():
            self.memory_file.unlink()
        
        self._memory_data = self._load_memory()
        print("🗑️ 所有长期记忆已清空")


# ===== 快捷使用函数 =====

_memory_instance: Optional[WukongMemory] = None


def get_memory() -> WukongMemory:
    """获取记忆管理器单例"""
    global _memory_instance
    if _memory_instance is None:
        _memory_instance = WukongMemory()
    return _memory_instance


def read_context() -> SessionContext:
    """快捷函数: 读取记忆上下文"""
    return get_memory().read_memory()


def save_session(session_data: Dict[str, Any]) -> None:
    """快捷函数: 保存会话数据"""
    get_memory().update_memory(session_data)


def remember(description: str, importance: int = 3) -> None:
    """快捷函数: 记住重要事情"""
    get_memory().add_important_memory(description, importance=importance)


if __name__ == "__main__":
    # 测试代码
    print("🧪 测试悟空记忆系统\n")
    
    # 1. 读取记忆
    memory = WukongMemory()
    context = memory.read_memory()
    print(f"\n加载的上下文: {context}\n")
    
    # 2. 更新记忆
    memory.update_memory({
        "session_summary": "用户测试了记忆系统",
        "new_preferences": {"test_mode": True},
        "key_points": ["用户喜欢简洁的回答", "用户关注性能优化"],
        "topics_discussed": ["记忆系统", "长期记忆"]
    })
    
    # 3. 查看摘要
    print(f"\n{memory.get_memory_summary()}")
