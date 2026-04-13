# wnews 五维进化系统 - 工作记忆

## 项目架构
- **v3系统**: `news-server/` - 原有四层分析（沙僧→白龙马→八戒融合）
- **v4系统**: `news-evolution/` - 五维进化增强（悟空→沙僧→白龙马→八戒→唐僧仲裁）
- **数据隔离**: 两套系统完全独立，v4通过sys.path引用v3模块

## 五维进化体系
| 角色 | 职责 | 经验库位置 |
|------|------|------------|
| 🐵 悟空增强 | S/A级新闻分析，地缘+Trump+财报 | market_agents_evolution/ |
| 🧔 沙僧增强 | 散户情绪预测，FOMO/逆向/拐点 | market_agents_evolution/ |
| 🐉 白龙马增强 | 主力行为推断，Trump模式识别 | market_agents_evolution/ |
| 🐷 八戒校准 | 贝叶斯概率计算，历史先验校准 | market_agents_evolution/ |
| 🙏 唐僧仲裁 | 跨层矛盾仲裁+全局风控，金色主题 | tang_seng_arbiter.py |

## 自动化任务
- **早报**: 09:00 - `wnews-早报09点`
- **晚报**: 20:00 - `wnews-晚报20点` ✅ 本次执行
- **复盘**: 周五17:00 - `wnews-周五复盘`

## 执行流程
1. `search_today.py` - 搜索今日新闻
2. `daily_update_v4.py` - 五维进化分析
3. 推送到 `wnews` 仓库 → https://xttey001.github.io/wnews/

## 历史修复记录
- 2026-04-12: 修复唐僧仲裁参数错误 (`bajie_enhanced` → `bajie_calibrated`)
