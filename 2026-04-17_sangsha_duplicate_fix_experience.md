# JSON 重复 Key 覆盖问题修复经验

**时间**：2026-04-17 00:33  
**项目**：wnews 财经新闻网站  
**问题**：沙僧模块逐条分析新闻标题显示为空

---

## 问题现象

用户访问 https://xttey001.github.io/wnews/ 时，沙僧模块的 `analysis_results` 中每条新闻的标题显示为空白：

```
分析全量新闻 0 条  ← 实际有 7-9 条新闻
```

---

## 根因分析

### 第一层：字段名不匹配？

最初怀疑 `news` 字段和 `title` 字段命名不一致。

**验证**：检查 news-data.js，发现 sangsha_module 中同时有 `news` 和 `title` 字段，且 `news` = 简短版标题，`title` = 完整标题。

**结论**：字段命名无问题。

### 第二层：JSON 语法错误？

怀疑 JSON 语法错误导致解析中断。

**验证**：运行 `node --check news-data.js` → 无错误。

**结论**：语法正确。

### 第三层：重复 Key 覆盖（根因）

**发现**：每个日期存在 **两个 `sangsha_module`**！

```javascript
// 第一个 sangsha_module（正确的）
"sangsha_module": {
  "analysis_results": [
    {
      "title": "一季度GDP同比增5.0%，中国经济开局良好",  // ✅ 有 title
      "full_title": "...",
      "韭菜行为总结": "散户情绪高涨，积极做多",
      "市场含义": "利好兑现",
      // ...完整字段
    }
  ]
}

// 第二个 sangsha_module（简化的）
"sangsha_module": {
  "analysis_results": [
    {
      "news": "一季度GDP增5%超预期",  // ❌ 只有 news，没有 title！
      "买入概率": 82,
      "情绪标签": ["FOMO", "易懂"]
      // ...缺失大量字段
    }
  ]
}
```

**JavaScript 解析行为**：后者覆盖前者，导致 `analysis_results[0].title` 为 `undefined`。

---

## 修复方案

### 1. 编写检测脚本

```javascript
const content = fs.readFileSync('news-data.js', 'utf-8');
const dates = ['2026-04-14', '2026-04-15', '2026-04-16'];

dates.forEach(date => {
  const block = extractBlock(content, date);
  const matches = block.match(/sangsha_module/g);
  console.log(date + ': sangsha_module count =', matches ? matches.length : 0);
});
```

**输出**：
```
2026-04-14: sangsha_module count = 2
2026-04-15: sangsha_module count = 2
2026-04-16: sangsha_module count = 2
```

### 2. 删除重复模块

编写 `remove_duplicate_sangsha.js`：
1. 定位第一个 sangsha_module 的结束位置
2. 删除第二个 sangsha_module（包括前面的逗号）
3. 保持 JSON 语法正确

### 3. 验证修复

```bash
node --check news-data.js  # 语法 OK
node verify_sangsha_fixed.js  # 每个 date 只有 1 个 sangsha_module，字段完整
```

**输出**：
```
2026-04-14: sangsha_module count = 1
  has title: true
  has full_title: true
  has 韭菜行为总结: true
```

### 4. 推送 GitHub

```bash
git add news-data.js
git commit -m "Fix: 删除重复的sangsha_module，保留完整字段版本"
git push
```

---

## 核心教训

### ❌ 错误认知

"JSON 语法正确 = 数据正确"

### ✅ 正确认知

"JSON 语法正确 ≠ 数据结构正确"

JavaScript 对象中**同一 key 重复不会报错**，只会静默覆盖：
```javascript
const obj = {
  "a": 1,
  "a": 2
};
console.log(obj.a);  // 输出: 2（没有报错，但数据丢失了）
```

---

## 预防措施

### 1. 数据生成脚本必须检查 key 是否存在

```python
# 错误做法
data["sangsha_module"] = new_analysis  # 直接覆盖

# 正确做法
if "sangsha_module" in data:
    # 合并或更新
    data["sangsha_module"].update(new_analysis)
else:
    data["sangsha_module"] = new_analysis
```

### 2. 写入后运行验证脚本

```javascript
// 检查每个日期的关键模块数量
const criticalKeys = ['sangsha_module', 'white_dragon', 'bajie_conclusion', 'wukong_judgment'];
dates.forEach(date => {
  criticalKeys.forEach(key => {
    const count = countOccurrences(block, key);
    if (count !== 1) {
      console.error(`⚠️ ${date}: ${key} appears ${count} times (expected 1)`);
    }
  });
});
```

### 3. 前端渲染时做空值保护

```javascript
// 错误做法
const title = item.title;  // 可能为 undefined

// 正确做法
const title = item.title || item.news || '未知标题';
```

---

## 更新的文件

| 文件 | 更新内容 |
|------|---------|
| `MEMORY.md` | 新增「JSON 数据结构防故障经验」章节 |
| `skills/wnews-dashboard/SKILL.md` | 新增「禁止同一层级存在重复 key」检查清单 |

---

## 相关 Commit

- `eb88406` - Fix: 删除重复的sangsha_module，保留完整字段版本
- `20faa74` - Fix: 修复04-14/15/16沙僧模块 - 全量新闻分析+完整字段（上一个 commit，未解决问题）
