# 🐵 悟空长期记忆系统

实现"**先查看长期记忆，再更新**"的机制，让AI助手能够记住用户偏好和对话历史。

## 核心原理

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   对话开始      │────→│  1. 读取记忆    │────→│  2. 加载上下文  │
│                 │     │  (Read First)   │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
┌─────────────────┐     ┌─────────────────┐            ▼
│   对话结束      │←────│  4. 更新记忆    │←─── 3. 执行对话任务
│   (Save)        │     │  (Update)       │
└─────────────────┘     └─────────────────┘
```

## 文件说明

| 文件 | 作用 |
|------|------|
| `wukong_memory.py` | 核心记忆管理类 |
| `session_start.py` | 会话启动入口 - 读取记忆 |
| `session_end.py` | 会话结束出口 - 保存记忆 |
| `example_usage.py` | 使用示例 |

## 快速开始

### 1. 基本使用

```python
from wukong_memory import WukongMemory

# 创建记忆管理器
memory = WukongMemory()

# 会话开始 - 先读取记忆
context = memory.read_memory()
print(f"已进行 {context.session_count} 次对话")

# ... 处理用户请求 ...

# 会话结束 - 再更新记忆
memory.update_memory({
    "session_summary": "用户询问了记忆系统",
    "key_points": ["用户喜欢简洁回答"],
    "new_preferences": {"style": "简洁"}
})
```

### 2. 使用快捷函数

```python
from wukong_memory import read_context, save_session, remember

# 读取记忆
context = read_context()

# ... 对话中 ...

# 保存会话
save_session({
    "session_summary": "摘要",
    "key_points": ["要点1", "要点2"]
})

# 记录重要事情
remember("用户使用Python", importance=4)
```

### 3. 命令行使用

**查看记忆状态:**
```bash
python example_usage.py --status
```

**手动保存会话:**
```bash
# 交互式
python session_end.py

# 快速保存
python session_end.py -q "本次对话摘要"

# 带关键要点
python session_end.py -s "摘要" -k "要点1" "要点2"
```

## 在项目中集成

### 集成到 Skill 系统

在悟空 Skill 中添加记忆功能:

```python
from memory.wukong_memory import read_context, save_session

def wukong_handler(user_query: str):
    # 1. 先读取记忆
    context = read_context()
    
    # 2. 将记忆注入提示词
    memory_prompt = f"""
【长期记忆】
- 会话次数: {context.session_count}
- 用户偏好: {context.user_preferences}
- 关键记忆: {context.key_learnings}

【用户问题】
{user_query}
"""
    
    # 3. 处理请求
    response = process_with_ai(memory_prompt)
    
    # 4. 保存记忆
    save_session({
        "session_summary": extract_summary(response),
        "key_points": extract_key_points(response)
    })
    
    return response
```

### 自动执行

在 `AGENTS.md` 中添加启动/结束钩子:

```python
# 会话启动时自动执行
# memory/session_start.py

# 会话结束时自动执行
# memory/session_end.py --quick "自动保存的摘要"
```

## 数据结构

### SessionContext (会话上下文)

```python
{
    "user_preferences": {},      # 用户偏好
    "recent_topics": [],         # 最近话题
    "key_learnings": [],         # 关键学习点
    "session_count": 0,          # 会话次数
    "last_session_date": ""      # 上次会话日期
}
```

### update_memory 参数

```python
{
    "session_summary": "str",           # 会话摘要
    "key_points": ["str"],              # 关键要点
    "topics_discussed": ["str"],        # 讨论话题
    "new_preferences": {"key": "val"},  # 新偏好
    "important_events": ["str"]         # 重要事件
}
```

## 存储位置

记忆文件保存在: `memory/wukong_long_term_memory.json`

## 使用示例

运行示例查看完整流程:

```bash
# 运行所有示例
python example_usage.py

# 运行指定示例
python example_usage.py -e 1
python example_usage.py -e 2
python example_usage.py -e 3

# 查看当前记忆状态
python example_usage.py -s
```

## 注意事项

1. **先读后写**: 严格遵循"先读取记忆，再更新记忆"的顺序
2. **不要重复保存**: 一次会话只保存一次记忆
3. **重要性分级**: 使用 importance 参数标记关键记忆 (1-5)
4. **隐私保护**: 敏感信息不要存入长期记忆

## 进阶用法

### 添加重要记忆

```python
from wukong_memory import remember

# 在对话中随时记录
remember("用户使用PostgreSQL", importance=4)
remember("用户对性能敏感", importance=3)
```

### 查看记忆摘要

```python
from wukong_memory import WukongMemory

memory = WukongMemory()
print(memory.get_memory_summary())
```

### 清空记忆 (谨慎!)

```python
memory.clear_memory(confirm=True)
```
