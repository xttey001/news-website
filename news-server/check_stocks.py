with open(r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\news-data.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Find first occurrence of "stocks"
idx = c.find('"stocks"')
print('Position:', idx)
# Show 300 chars around it
print(repr(c[idx:idx+400]))
