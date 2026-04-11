# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'C:\Users\asus\.qclaw\workspace\MEMORY.md', encoding='utf-8') as f:
    content = f.read()

start = content.find('### 财经新闻四层分析系统（2026-04-10 确定）')
end = content.find('## QClaw获取新闻流程（已废弃，用generate_full_newsdata.py代替）')

new_section = """### 财经新闻四层分析系统（2026-04-10 确定，含三层交叉分析）

### 架构图
```
原始新闻
   ↓                    ← 完全独立的两条链
悟空+八戒 ←──┐           │
             │           │  ← 互相不看（已修复）
沙僧+白龙马 ─┘           │
   ↓                    │
市场数据                 │
   ↓                    │
沙僧 ←── 白龙马 ←── 八戒  ←  ← 三层交叉分析
```

### 四角色定位
- **悟空**：新闻分析师，基于S/A级新闻做情绪判断+操作策略
- **八戒**：概率分析师，基于S/A级新闻计算贝叶斯胜率+ETF推荐
- **沙僧**：散户行为预测，基于**全部新闻**（含噪音）7天累积+时间衰减
- **白龙马**：主力意图推断，基于全部新闻+K线+成交量

### 三层交叉分析（核心设计）

**第一层：白龙马融合悟空信号**
- 悟空情绪 vs 白龙马主力状态 → 矛盾检测
- 悟空积极 + 白龙马出货 → 可信度×0.7
- 悟空恐慌 + 白龙马吸筹 → 逆向机会×1.2

**第二层：八戒融合沙僧+白龙马信号**
- 沙僧狂热 + 八戒胜率>60% → 胜率降至35%（追高即被套）
- 白龙马出货 → ETF推荐改为"减仓回避"
- 信号一致性评分：3分=共振，2分=正常，1分=混乱

**关键脚本**
- `market_agents/white_dragon_model.py` v2：融合悟空/八戒信号
- `market_agents/bajie_model.py` v2：融合沙僧+白龙马信号
- `generate_full_newsdata.py` v2：串联三层交叉分析

### 数据格式（融合后八戒结论）
- optimal_action: 最终行动（含融合调整）
- win_rate: "~38%（贝叶斯后验+沙僧白龙马融合）"
- 沙僧信号: {情绪, 平均买入概率, 调整结果}
- 白龙马信号: {主力状态, 是否利用散户, 风险等级, 调整结果}
- 信号一致性: 得分+文字说明
- 融合说明: ["【沙僧融合】...", "【白龙马融合】..."]

"""

if start == -1 or end == -1:
    print(f'start={start}, end={end}')
    print('Cannot find boundaries')
    exit(1)

print(f'start={start}, end={end}')
new_content = content[:start] + new_section + content[end:]
print(f'before: {len(content)}, after: {len(new_content)}')

with open(r'C:\Users\asus\.qclaw\workspace\MEMORY.md', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('MEMORY.md updated!')
