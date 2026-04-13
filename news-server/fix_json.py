import re
with open('news_data/news_2026-04-13.json', 'r', encoding='utf-8') as f:
    content = f.read()
# 替换所有中文引号为英文单引号
content = content.replace('\u201c', "'").replace('\u201d', "'")
# 替换中文书名号为英文书名号
content = content.replace('\u300a', '<').replace('\u300b', '>')
with open('news_data/news_2026-04-13.json', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed all Chinese quotes')
