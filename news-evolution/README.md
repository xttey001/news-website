# 🧬 悟空财经进化系统（news-evolution）

## 与原有系统的关系

| 项目 | 路径 | 说明 |
|------|------|------|
| **原有系统** | `workspace/news-server/` | qclaw 原始新闻系统（不动） |
| **进化系统** | `workspace/news-evolution/` | 五维进化增强（本项目） |
| **网站仓库** | `c:/Users/asus/wnews/` | GitHub Pages 部署 |

## 目录结构

```
news-evolution/
├── market_agents_evolution/     ← 进化模块（独立于原有模型）
│   ├── __init__.py
│   ├── wukong_enhanced.py       ← 🐵 悟空经验注入（地缘非线性/Trump量化/财报分级）
│   ├── sangsha_enhanced.py      ← 🧔 沙僧经验注入（FOMO预警/恐慌逆向/拐点预判）
│   ├── white_dragon_enhanced.py ← 🐉 白龙马经验注入（Trump-主力模式/出货vs洗盘/量价背离）
│   ├── bajie_enhanced.py        ← 🐷 八戒概率校准（先验库/信号权重/地缘有效期）
│   └── tang_seng_arbiter.py     ← 🙏 唐僧仲裁（跨层矛盾/全局风控）
├── data/
│   ├── review-experience.json   ← 经验知识库（12条经验+2条教训）
│   ├── pending_validations.json ← 待验证队列
│   └── validation_results.json  ← 验证结果
├── daily_update_v4.py           ← 进化版主脚本
├── validate_outcomes.py         ← 验证脚本（待实现）
├── weekly_review.py             ← 周五复盘（待实现）
└── README.md
```

## 执行流程

```
v4 主脚本 (daily_update_v4.py):
  Step 1:  搜索新闻（调用原有 search_today.py）
  Step 2:  导入模块（原有+进化）
  Step 3:  加载新闻
  Step 4:  构建场景元数据（地缘/Trump/财报季等标签）
  Step 5:  原有四层分析（沙僧→白龙马→八戒融合）
  Step 6:  🧬 五维进化增强（悟空增强→沙僧增强→白龙马增强→八戒校准→唐僧仲裁）
  Step 7:  组装最终输出
  Step 8:  写入新闻文件（追加进化标注，不覆盖原有字段）
  Step 9:  存入待验证队列
  Step 10: 生成 news-data.js
  Step 11: 推送到 wnews 仓库
```

## 运行方式

```bash
cd c:\Users\asus\.qclaw\workspace\news-evolution
python daily_update_v4.py
```

## 经验库更新

编辑 `data/review-experience.json` 添加新经验，格式见 SKILL.md。
