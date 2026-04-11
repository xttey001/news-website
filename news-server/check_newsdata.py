# -*- coding: utf-8 -*-
import glob, json
files = sorted(glob.glob('news_data/news_*.json'), reverse=True)
print('Files found:', len(files))
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', 'N/A')
    s_count = len(d.get('s_level', []))
    has_wk = bool(d.get('wukong_judgment'))
    print('  ' + date + ': s=' + str(s_count) + ' wk=' + str(has_wk))
