import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\asus\.qclaw\workspace\news-data.js', 'r', encoding='utf-8', errors='replace') as f:
    raw_text = f.read()

raw_text = raw_text.replace('\r\n', '\n').replace('\r', '\n')

def extract_entry(raw_text, target_date):
    pattern = f'"{target_date}":\\s*\\{{'
    m = re.search(pattern, raw_text)
    if not m:
        return None
    
    start = m.start()
    depth = 0
    end = start
    in_string = False
    escape_next = False
    
    for i in range(start, len(raw_text)):
        c = raw_text[i]
        if escape_next:
            escape_next = False
            continue
        if c == '\\' and in_string:
            escape_next = True
            continue
        if c == '"' and not escape_next:
            in_string = not in_string
            continue
        if in_string:
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    
    entry_text = raw_text[start:end]
    obj_text = entry_text[entry_text.index('{'):]
    return json.loads(obj_text)

results = {}
for d in ['2026-04-07', '2026-04-08', '2026-04-09', '2026-04-10']:
    entry = extract_entry(raw_text, d)
    if entry:
        results[d] = entry
        print(f"\n{'='*60}")
        print(f"DATE: {d}")
        print(f"market_tone: {entry.get('market_tone', 'N/A')}")
        
        # Wukong judgment
        wj = entry.get('wukong_judgment', {})
        print(f"\n[悟空判断] emotion: {wj.get('emotion', 'N/A')}")
        if 'analysis' in wj and wj['analysis']:
            for a in wj['analysis']:
                print(f"  analysis: {a[:100]}")
        elif 'strategy' in wj:
            for s in wj['strategy']:
                print(f"  strategy: {s[:100]}")
        else:
            print(f"  (no analysis/strategy found, keys: {list(wj.keys())})")
        
        # Bajie conclusion
        bj = entry.get('bajie_conclusion', {})
        if bj:
            print(f"\n[八戒贝叶斯]")
            for k, v in bj.items():
                if isinstance(v, str):
                    print(f"  {k}: {v[:100]}")
                elif isinstance(v, dict):
                    print(f"  {k}: {v}")
                else:
                    print(f"  {k}: {v}")
        
        # S-level news
        s_news = entry.get('s_level', [])
        print(f"\n[S级新闻] count={len(s_news)}")
        for n in s_news[:3]:
            print(f"  [{n.get('emoji','')}] {n.get('title','')[:80]}")
            print(f"    sentiment: {n.get('signal','')[:100]}")
        
        # White dragon
        wd = entry.get('white_dragon', {})
        if wd:
            print(f"\n[白龙马] keys={list(wd.keys())}")
            if 'main_state' in wd:
                print(f"  main_state: {wd['main_state']}")
            if '综合建议' in wd:
                print(f"  综合建议: {wd['综合建议'][:100]}")

print(f"\n{'='*60}")
print(f"Successfully extracted {len(results)} date entries")

# Save all results
with open('all_review_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved to all_review_data.json")
