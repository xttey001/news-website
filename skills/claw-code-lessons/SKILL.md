# Claw Code Lessons

从 ultraworkers/claw-code 仓库学习到的最佳实践和设计模式。

## 核心理念

> "Humans set direction; claws perform the labor."

Claw Code 展示了如何用 AI Agent 系统自主构建和维护大型项目：
- 人类提供方向和决策
- AI Agent（claws）执行具体工作
- 通过聊天界面进行协作

## 三层协调系统

### 1. OmX (oh-my-codex) - 工作流层
- 将简短指令转化为结构化执行
- 规划关键词（如 `$team`, `$ralph`）
- 持久化验证循环
- 并行多 Agent 工作流

### 2. clawhip - 事件和通知路由器
- 监控 git commits、tmux sessions、GitHub issues/PRs
- **关键原则**: 将监控和通知移出 Agent 的上下文窗口
- 让 Agent 专注实现而非状态格式化

### 3. OmO (oh-my-openagent) - 多 Agent 协调
- 规划、交接、分歧解决
- 验证循环
- Architect/Executor/Reviewer 角色协作

## 代码组织模式

```
project/
├── crates/ or src/
│   ├── api/              # API 客户端 + 流解析
│   ├── commands/         # 命令注册表
│   ├── runtime/          # 会话、配置、权限
│   ├── tools/            # 工具实现
│   ├── plugins/          # 插件系统
│   └── telemetry/        # 追踪和遥测
```

## 关键设计原则

### 权限系统
- `read-only` - 只读模式
- `workspace-write` - 工作区写入
- `danger-full-access` - 完全访问

### 会话管理
- 会话持久化
- 支持 resume 恢复
- 成本追踪和用量显示
- 最大轮次和预算限制

### 配置层级（优先级从低到高）
1. `~/.claw.json`
2. `~/.config/claw/settings.json`
3. `<repo>/.claw.json`
4. `<repo>/.claw/settings.json`
5. `<repo>/.claw/settings.local.json`

### 工具系统最佳实践
- 每个工具有清晰的权限上下文
- 支持按权限过滤工具
- 简单模式（只暴露核心工具）
- MCP 工具可选包含

## Python 实现模式

### QueryEngine 配置
```python
@dataclass(frozen=True)
class QueryEngineConfig:
    max_turns: int = 8              # 最大对话轮次
    max_budget_tokens: int = 2000   # Token 预算
    compact_after_turns: int = 12   # 自动压缩阈值
```

### 工具权限上下文
```python
def filter_tools_by_permission_context(
    tools: tuple[Tool, ...],
    permission_context: ToolPermissionContext | None = None
) -> tuple[Tool, ...]
```

### 会话存储模式
```python
@dataclass
class QueryEnginePort:
    manifest: PortManifest
    config: QueryEngineConfig
    session_id: str
    mutable_messages: list[str]
    transcript_store: TranscriptStore
```

## 应用到当前工作

### 当用户要求复杂任务时
1. 使用 `$team` 模式分解任务
2. 明确 Architect/Executor/Reviewer 角色
3. 设置清晰的验证循环

### 当处理长对话时
1. 监控 token 使用量
2. 达到阈值时主动 compact
3. 保持关键上下文，移除冗余

### 当设计工具系统时
1. 为每个工具定义权限级别
2. 支持按上下文过滤
3. 保持工具描述简洁明确

## 参考链接

- claw-code: https://github.com/ultraworkers/claw-code
- clawhip: https://github.com/Yeachan-Heo/clawhip
- oh-my-codex: https://github.com/Yeachan-Heo/oh-my-codex
- oh-my-openagent: https://github.com/code-yeongyu/oh-my-openagent
