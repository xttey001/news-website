#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新闻数据拆分脚本 - 简化版
将 news-data.js 中的数据按日期拆分为独立的 JSON 文件
"""

import json
import re
from pathlib import Path
from datetime import datetime


def extract_date_sections(file_path):
    """从 JS 文件中提取每个日期的原始文本"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到 newsData = { 之后的部分
    match = re.search(r'const\s+newsData\s*=\s*\{', content)
    if not match:
        raise ValueError("无法找到 newsData 对象")
    
    # 提取所有日期键
    date_pattern = r'"(\d{4}-\d{2}-\d{2})"\s*:\s*\{'
    dates = []
    
    for m in re.finditer(date_pattern, content):
        dates.append({
            'date': m.group(1),
            'start': m.start()
        })
    
    print(f"找到 {len(dates)} 个日期")
    
    # 为每个日期提取内容
    date_sections = {}
    
    for i, date_info in enumerate(dates):
        date_str = date_info['date']
        start_pos = date_info['start']
        
        # 找到这个日期数据的结束位置
        if i < len(dates) - 1:
            # 不是最后一个，结束位置是下一个日期的开始
            end_pos = dates[i + 1]['start']
            # 向前找逗号或结束括号
            while end_pos > start_pos and content[end_pos - 1] in ' \t\n,':
                end_pos -= 1
        else:
            # 最后一个日期，需要找到 newsData 的结束
            # 从 start_pos 开始找匹配的 }
            brace_count = 0
            pos = content.find('{', start_pos) + 1
            while pos < len(content):
                if content[pos] == '{':
                    brace_count += 1
                elif content[pos] == '}':
                    if brace_count == 0:
                        break
                    brace_count -= 1
                pos += 1
            end_pos = pos
        
        # 提取完整的日期条目（包含键名）
        section = content[start_pos:end_pos]
        date_sections[date_str] = section
        print(f"✓ 提取: {date_str} ({len(section)} 字符)")
    
    return date_sections


def js_to_json(js_text):
    """将 JavaScript 对象文本转换为标准 JSON"""
    # 移除开头的 "date": 
    js_text = re.sub(r'^\s*"\d{4}-\d{2}-\d{2}"\s*:\s*', '', js_text)
    
    # 移除 trailing commas
    js_text = re.sub(r',(\s*[}\]])', r'\1', js_text)
    
    # 确保所有 key 都有引号
    # 匹配未被引号包围的 key
    js_text = re.sub(r'([{,]\s*)([a-zA-Z_\u4e00-\u9fa5][a-zA-Z0-9_\u4e00-\u9fa5]*)\s*:', r'\1"\2":', js_text)
    
    return js_text


def parse_and_save(date_sections, output_dir):
    """解析并保存每个日期的数据"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    available_dates = []
    
    for date_str, js_section in date_sections.items():
        try:
            # 转换为 JSON
            json_text = js_to_json(js_section)
            
            # 解析为 Python 对象
            data = json.loads(json_text)
            data['date'] = date_str
            
            # 保存为 JSON 文件
            file_path = output_path / f"{date_str}.json"
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            available_dates.append(date_str)
            print(f"✓ 保存: {file_path}")
            
        except json.JSONDecodeError as e:
            print(f"⚠ JSON 解析失败 {date_str}: {e}")
            # 尝试使用 ast.literal_eval
            try:
                import ast
                # 移除开头的 "date": 
                clean_text = re.sub(r'^\s*"\d{4}-\d{2}-\d{2}"\s*:\s*', '', js_section)
                # 移除 trailing commas
                clean_text = re.sub(r',(\s*[}\]])', r'\1', clean_text)
                data = ast.literal_eval(clean_text)
                data['date'] = date_str
                
                file_path = output_path / f"{date_str}.json"
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                available_dates.append(date_str)
                print(f"✓ 使用 ast 保存: {file_path}")
            except Exception as e2:
                print(f"❌ 完全失败 {date_str}: {e2}")
    
    # 按日期降序排序
    available_dates.sort(reverse=True)
    return available_dates


def create_index_file(available_dates, output_path):
    """创建日期索引文件"""
    index_data = {
        "availableDates": available_dates,
        "lastUpdated": datetime.now().isoformat(),
        "totalCount": len(available_dates),
        "version": "1.0"
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 索引: {output_path}")


def create_loader_js(output_path):
    """创建数据加载器"""
    loader_code = '''// 新闻数据加载器 - 按需加载指定日期
const NewsDataLoader = {
	cache: {},
	index: null,
	
	async loadIndex() {
		if (this.index) return this.index;
		const res = await fetch('./news-data-index.json');
		this.index = await res.json();
		return this.index;
	},
	
	async loadDate(date) {
		if (this.cache[date]) return this.cache[date];
		const res = await fetch(`./news-data/${date}.json`);
		const data = await res.json();
		this.cache[date] = data;
		return data;
	},
	
	async getAvailableDates() {
		const index = await this.loadIndex();
		return index.availableDates;
	},
	
	async getLatestDate() {
		const dates = await this.getAvailableDates();
		return dates[0];
	}
};
'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(loader_code)
    print(f"✓ 加载器: {output_path}")


def main():
    workspace_dir = Path(__file__).parent.parent
    news_data_js = workspace_dir / 'news-data.js'
    news_data_dir = workspace_dir / 'news-data'
    index_file = workspace_dir / 'news-data-index.json'
    loader_file = workspace_dir / 'news-data-loader.js'
    
    print("=" * 50)
    print("新闻数据拆分工具")
    print("=" * 50)
    
    if not news_data_js.exists():
        print(f"❌ 错误: 找不到 {news_data_js}")
        return
    
    print(f"\n📖 读取: {news_data_js}\n")
    
    # 提取日期段落
    date_sections = extract_date_sections(news_data_js)
    
    # 解析并保存
    print(f"\n📁 保存到: {news_data_dir}\n")
    available_dates = parse_and_save(date_sections, news_data_dir)
    
    # 创建索引和加载器
    print(f"\n📋 创建辅助文件\n")
    create_index_file(available_dates, index_file)
    create_loader_js(loader_file)
    
    print("\n" + "=" * 50)
    print(f"✅ 完成! 共 {len(available_dates)} 个日期")
    print("=" * 50)


if __name__ == '__main__':
    main()
