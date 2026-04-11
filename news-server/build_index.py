# Read both parts and combine
with open(r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\index.html', 'r', encoding='utf-8') as f:
    part1 = f.read()

with open(r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\index_part2.html', 'r', encoding='utf-8') as f:
    part2 = f.read()

# The part1 ends with `}).catch` - we need to append part2 after it
# part2 starts with `}).catch...` and ends with `</html>`
# Remove the incomplete `}).catch` line from part1
idx = part1.find('}).catch(function() {')
if idx > 0:
    part1 = part1[:idx]

full = part1 + '\n' + part2

with open(r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\index.html', 'w', encoding='utf-8') as f:
    f.write(full)

print('Combined. Total length:', len(full))
print('Ends with:', full[-50:])
