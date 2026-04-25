# -*- coding: utf-8 -*-
"""
更新本地HTML页面脚本 V2
直接把 news-data.js 的内容嵌入到 local_news.html 中
"""
import re

# 路径配置
LOCAL_HTML_PATH = r'C:\Users\asus\.qclaw\workspace\local_news.html'
NEWS_DATA_PATH = r'C:\Users\asus\.qclaw\workspace\news-data.js'

def update_local_html():
    """更新本地HTML文件"""
    print("="*60)
    print("🔄 更新本地HTML页面 V2")
    print("="*60)
    
    # 读取 news-data.js 完整内容
    try:
        with open(NEWS_DATA_PATH, 'r', encoding='utf-8') as f:
            js_content = f.read()
        print(f"✅ 已读取: {NEWS_DATA_PATH}")
        print(f"   文件大小: {len(js_content)} 字符")
    except Exception as e:
        print(f"❌ 读取 news-data.js 失败: {e}")
        return False
    
    # 读取 local_news.html
    try:
        with open(LOCAL_HTML_PATH, 'r', encoding='utf-8') as f:
            html_content = f.read()
        print(f"✅ 已读取: {LOCAL_HTML_PATH}")
    except Exception as e:
        print(f"❌ 读取 local_news.html 失败: {e}")
        return False
    
    # 使用标记替换方式
    if '<!-- DATA_JS_START -->' not in html_content:
        print("⚠️ 未找到数据标记，重新构建HTML结构...")
        
        # 构建新的HTML结构
        new_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>悟空财经分析 - 本地版</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{
            --bg-start: #0d1117; --bg-end: #161b22;
            --green: #3fb950; --green-bg: rgba(63,185,80,0.12);
            --orange: #f0883e; --red: #f85149;
            --blue: #58a6ff; --gold: #d29922; --purple: #a371f7;
            --card-bg: rgba(255,255,255,0.04);
            --card-border: rgba(255,255,255,0.1);
            --text: #e6edf3; --text-dim: #8b949e;
            --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }}
        body {{ font-family: var(--font); background: linear-gradient(135deg, var(--bg-start) 0%, var(--bg-end) 100%); color: var(--text); min-height: 100vh; padding: 20px; line-height: 1.7; }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        .header {{ text-align: center; margin-bottom: 32px; padding: 24px; background: var(--card-bg); border-radius: 16px; border: 1px solid var(--card-border); }}
        .header h1 {{ font-size: 26px; margin-bottom: 4px; background: linear-gradient(135deg, var(--green) 0%, var(--blue) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .header .subtitle {{ font-size: 13px; color: var(--text-dim); margin-bottom: 8px; font-style: italic; }}
        .header .date-tag {{ display: inline-block; margin-top: 10px; padding: 6px 14px; background: rgba(163,113,247,0.15); border: 1px solid rgba(163,113,247,0.3); border-radius: 8px; color: var(--purple); font-size: 13px; }}
        .local-badge {{ display: inline-block; margin-top: 8px; padding: 4px 10px; background: rgba(63,185,80,0.15); border: 1px solid rgba(63,185,80,0.3); border-radius: 6px; color: var(--green); font-size: 11px; }}
        .nav-bar {{ display: flex; justify-content: center; gap: 8px; margin-bottom: 28px; flex-wrap: wrap; padding: 14px; background: var(--card-bg); border-radius: 12px; border: 1px solid var(--card-border); }}
        .date-btn {{ padding: 8px 16px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; cursor: pointer; transition: all 0.3s; font-size: 13px; color: var(--text-dim); }}
        .date-btn:hover {{ background: rgba(63,185,80,0.1); border-color: var(--green); color: var(--green); }}
        .date-btn.active {{ background: var(--green-bg); border-color: var(--green); color: var(--green); font-weight: 600; }}
        .section {{ background: var(--card-bg); border-radius: 14px; border: 1px solid var(--card-border); padding: 22px; margin-bottom: 24px; }}
        .section-title {{ font-size: 18px; font-weight: 600; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.1); }}
        .tone-section {{ border: 2px solid var(--gold); background: linear-gradient(135deg, rgba(210,153,34,0.08) 0%, rgba(210,153,34,0.03) 100%); }}
        .tone-section .section-title {{ color: var(--gold); }}
        .tone-item {{ margin-bottom: 12px; padding: 10px; background: rgba(0,0,0,0.15); border-radius: 6px; }}
        .tone-label {{ font-weight: 600; color: var(--gold); margin-right: 8px; }}
        .judgment-section {{ background: linear-gradient(135deg, rgba(163,113,247,0.08) 0%, rgba(88,166,255,0.05) 100%); border-color: rgba(163,113,247,0.2); }}
        .judgment-section .section-title {{ color: var(--purple); }}
        .emotion-row {{ font-size: 14px; margin-bottom: 14px; padding-bottom: 14px; border-bottom: 1px solid rgba(255,255,255,0.08); }}
        .emotion-label {{ color: var(--text-dim); }}
        .emotion-value {{ color: var(--green); font-weight: 600; }}
        .analysis-item {{ position: relative; padding-left: 18px; margin-bottom: 10px; font-size: 14px; }}
        .analysis-item::before {{ content: '•'; position: absolute; left: 0; color: var(--text-dim); }}
        .strategy-box {{ background: linear-gradient(135deg, rgba(63,185,80,0.15) 0%, rgba(63,185,80,0.08) 100%); border: 1px solid rgba(63,185,80,0.3); border-radius: 10px; padding: 16px; margin-top: 8px; }}
        .strategy-label {{ font-size: 13px; color: var(--green); font-weight: 600; margin-bottom: 10px; }}
        .strategy-item {{ font-size: 14px; margin-bottom: 8px; }}
        .news-section.s-level .section-title {{ color: var(--red); }}
        .news-section.a-level .section-title {{ color: var(--gold); }}
        .news-card {{ background: rgba(255,255,255,0.03); border-radius: 12px; border-left: 4px solid; padding: 18px; margin-bottom: 16px; }}
        .s-level .news-card {{ border-left-color: var(--red); }}
        .a-level .news-card {{ border-left-color: var(--gold); }}
        .news-header {{ display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; margin-bottom: 12px; }}
        .news-title {{ font-size: 16px; font-weight: 600; color: #fff; flex: 1; }}
        .news-source {{ padding: 4px 10px; background: rgba(255,255,255,0.06); border-radius: 6px; font-size: 11px; color: var(--text-dim); }}
        .label {{ color: var(--text-dim); margin-right: 6px; font-size: 13px; }}
        .tags-wrap {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }}
        .tag-item {{ display: inline-flex; align-items: center; border-radius: 6px; overflow: hidden; font-size: 12px; border: 1px solid rgba(255,255,255,0.15); }}
        .tag-sentiment {{ padding: 5px 8px; font-weight: 700; font-size: 11px; }}
        .tag-sentiment.bullish {{ background: var(--red); color: #fff; }}
        .tag-sentiment.bearish {{ background: var(--green); color: #fff; }}
        .tag-name {{ padding: 5px 10px; color: var(--text); }}
        .warning-box {{ margin-top: 14px; padding: 12px 14px; background: rgba(248,129,73,0.1); border: 1px solid rgba(248,129,73,0.25); border-radius: 8px; font-size: 13px; color: var(--orange); }}
        .section-divider {{ display: flex; align-items: center; margin: 32px 0; color: var(--text-dim); font-size: 14px; }}
        .section-divider::before, .section-divider::after {{ content: ''; flex: 1; height: 1px; background: linear-gradient(90deg, transparent, var(--card-border), transparent); }}
        .section-divider span {{ padding: 0 16px; }}
        footer {{ text-align: center; margin-top: 48px; padding: 24px; color: #484f58; font-size: 12px; }}
        .empty-state {{ text-align: center; padding: 60px 20px; }}
        .empty-state h3 {{ color: var(--text-dim); margin-bottom: 16px; }}
        .btn-primary {{ display: inline-block; margin-top: 20px; padding: 12px 24px; background: var(--green-bg); border: 1px solid var(--green); border-radius: 8px; color: var(--green); font-size: 14px; cursor: pointer; }}
        @media (max-width: 768px) {{ .header h1 {{ font-size: 22px; }} .section {{ padding: 16px; }} .news-card {{ padding: 14px; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🐵 悟空财经分析</h1>
            <div class="subtitle">不盲从主流解读，用逻辑和数据说话</div>
            <div class="date-tag" id="dateDisplay">加载中...</div>
            <div class="local-badge">📱 本地版 - 双击即用</div>
        </div>
        <div class="nav-bar" id="navBar"></div>
        <div id="content"></div>
        <footer>
            <p>数据来源：天集 ProSearch · 权威财经媒体</p>
            <p>本地文件路径：<span id="filePath"></span></p>
        </footer>
    </div>

<!-- DATA_JS_START -->
<script>
{js_content}
</script>
<!-- DATA_JS_END -->

<script>
// 页面渲染逻辑
document.getElementById('filePath').textContent = window.location.pathname;
let currentDate = availableDates[0];

function formatDate(dateStr) {{
    if (!dateStr) return '';
    const [y, m, d] = dateStr.split('-');
    return `${{parseInt(m)}}月${{parseInt(d)}}日`;
}}

function initNav() {{
    const navBar = document.getElementById('navBar');
    navBar.innerHTML = '';
    if (availableDates.length === 0) return;
    const recentDates = availableDates.slice(0, 7);
    recentDates.forEach(date => {{
        const btn = document.createElement('button');
        btn.className = 'date-btn' + (date === currentDate ? ' active' : '');
        btn.textContent = formatDate(date);
        btn.onclick = () => {{ currentDate = date; updateUI(); }};
        navBar.appendChild(btn);
    }});
}}

function updateUI() {{
    document.querySelectorAll('.date-btn').forEach(btn => {{
        btn.classList.toggle('active', formatDate(currentDate) === btn.textContent);
    }});
    document.getElementById('dateDisplay').textContent = availableDates.length > 0 ? formatDate(currentDate) : '暂无数据';
    renderContent();
}}

function getSentimentClass(s) {{
    const map = {{'利好':'bullish','利空':'bearish','关注':'watch','警惕':'avoid','回避':'avoid'}};
    return map[s] || 'neutral';
}}

function renderTags(items) {{
    if (!items?.length) return '';
    let html = '<div class="tags-wrap">';
    items.forEach(item => {{
        const isObj = typeof item === 'object' && item;
        const sentiment = isObj ? item.sentiment : '';
        const name = isObj ? item.name : item;
        html += `<span class="tag-item">`;
        if (sentiment) html += `<span class="tag-sentiment ${{getSentimentClass(sentiment)}}">${{sentiment}}</span>`;
        html += `<span class="tag-name">${{name}}</span></span>`;
    }});
    return html + '</div>';
}}

function renderNewsCard(item) {{
    let html = `<div class="news-card">
        <div class="news-header"><div class="news-title">${{item.emoji||''}} ${{item.title}}</div>${{item.source?`<div class="news-source">来源：${{item.source}}</div>`:''}}</div>
        <div class="news-row"><span class="label">要点：</span>${{item.key_point||item.summary||''}}</div>
        <div class="news-row"><span class="label">影响时长：</span>${{item.duration||'待定'}}</div>`;
    if (item.etfs?.length) html += `<div style="margin-top:10px"><span class="label">📈 ETF映射：</span>${{renderTags(item.etfs)}}</div>`;
    if (item.stocks?.length) html += `<div style="margin-top:10px"><span class="label">✨ 个股映射：</span>${{renderTags(item.stocks.map(s=>typeof s==='object'?s:{{name:s,sentiment:'利好'}}))}}</div>`;
    if (item.signal) html += `<div class="warning-box">💡 ${{item.signal}}</div>`;
    return html + '</div>';
}}

function renderEmptyState() {{
    return `<div class="section"><div class="empty-state"><h3>📭 暂无数据</h3><p>本地HTML页面需要先运行更新脚本</p><button class="btn-primary" onclick="location.reload()">刷新页面</button></div></div>`;
}}

function renderContent() {{
    const content = document.getElementById('content');
    const data = newsData[currentDate];
    if (!data) {{ content.innerHTML = renderEmptyState(); return; }}
    
    let html = '';
    if (data.market_tone) {{
        html += `<div class="section tone-section"><div class="section-title">📊 今日基调</div>`;
        if (typeof data.market_tone === 'object') {{
            if (data.market_tone.早报) html += `<div class="tone-item"><span class="tone-label">早报：</span>${{data.market_tone.早报}}</div>`;
            if (data.market_tone.晚报) html += `<div class="tone-item"><span class="tone-label">晚报：</span>${{data.market_tone.晚报}}</div>`;
        }} else html += `<div style="font-size:15px">${{data.market_tone}}</div>`;
        html += '</div>';
    }}
    
    if (data.wukong_judgment) {{
        const wj = data.wukong_judgment;
        html += `<div class="section judgment-section"><div class="section-title">📈 悟空今日判断</div>`;
        const emotion = wj.emotion || wj.market_sentiment;
        if (emotion) html += `<div class="emotion-row"><span class="emotion-label">大盘情绪：</span><span class="emotion-value">${{emotion}}</span></div>`;
        const analysis = wj.analysis || wj.core_analysis;
        if (analysis?.length) html += '<div>' + analysis.map(a=>`<div class="analysis-item">${{a}}</div>`).join('') + '</div>';
        const strategy = wj.strategy || wj.operations;
        if (strategy?.length) html += `<div class="strategy-box"><div class="strategy-label">今日操作参考：</div>${{strategy.map(s=>`<div class="strategy-item">${{s.type||''}} ${{s.content||s.action||s}}</div>`).join('')}}</div>`;
        html += '</div>';
    }}
    
    html += `<div class="section-divider"><span>=== 新闻详情 ===</span></div>`;
    
    if (data.s_level?.length) html += `<div class="section news-section s-level"><div class="section-title">🔴 S级（结构性叙事，影响1-4周）</div>${{data.s_level.map(renderNewsCard).join('')}}</div>`;
    if (data.a_level?.length) html += `<div class="section news-section a-level"><div class="section-title">🟡 A级（阶段性叙事，影响1-3天）</div>${{data.a_level.map(renderNewsCard).join('')}}</div>`;
    if (data.douyin?.length) html += `<div class="section news-section"><div class="section-title" style="color:var(--blue)">📱 抖音/平台相关</div>${{data.douyin.map(renderNewsCard).join('')}}</div>`;
    
    content.innerHTML = html;
}}

if (availableDates.length > 0) {{ initNav(); updateUI(); }}
else {{ document.getElementById('content').innerHTML = renderEmptyState(); document.getElementById('dateDisplay').textContent = '暂无数据'; }}
</script>
</body>
</html>'''
        
        # 写入文件
        try:
            with open(LOCAL_HTML_PATH, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"✅ 已创建新的本地HTML页面")
        except Exception as e:
            print(f"❌ 写入失败: {e}")
            return False
    else:
        # 使用标记替换
        pattern = r'<!-- DATA_JS_START -->.*?<!-- DATA_JS_END -->'
        replacement = f'<!-- DATA_JS_START -->\n<script>\n{js_content}\n</script>\n<!-- DATA_JS_END -->'
        
        html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
        
        try:
            with open(LOCAL_HTML_PATH, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"✅ 已更新本地HTML页面")
        except Exception as e:
            print(f"❌ 写入失败: {e}")
            return False
    
    print("="*60)
    print(f"🎉 本地HTML页面更新成功!")
    print(f"💡 提示: 双击 local_news.html 即可在浏览器中打开")
    print("="*60)
    return True

if __name__ == '__main__':
    update_local_html()
