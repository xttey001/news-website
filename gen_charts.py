import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib import rcParams
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS', 'DejaVu Sans']
rcParams['axes.unicode_minus'] = False

# 3月26日 申万行业板块涨幅TOP5数据
sectors = [
    {'name': '石油石化', 'change': 4.35, 'index': 17342.71},
    {'name': '能源装备', 'change': 2.89, 'index': 950.85},
    {'name': '煤炭开采', 'change': 2.27, 'index': 2175.63},
    {'name': '油气及制品', 'change': 2.19, 'index': 5014.91},
    {'name': '航运港口', 'change': 1.96, 'index': 4546.82},
]

names = [s['name'] for s in sectors]
changes = [s['change'] for s in sectors]
indices = [s['index'] for s in sectors]

colors = ['#FF4444', '#FF7744', '#FF9944', '#FFBB44', '#FFDD44']
colors_alpha = ['#FF444488', '#FF774488', '#FF994488', '#FFBB4488', '#FFDD4488']

OUTPUT_DIR = r'C:\Users\asus\.qclaw\workspace'

# ============================================================
# 1. 折线图
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(names, changes, 'o-', color='#FF4444', linewidth=2.5, markersize=10, markerfacecolor='white', markeredgewidth=2.5)
for i, (n, c) in enumerate(zip(names, changes)):
    ax.annotate(f'+{c}%', (n, c), textcoords='offset points', xytext=(0, 12), ha='center', fontsize=11, color='#FF4444', fontweight='bold')
ax.fill_between(names, changes, alpha=0.15, color='#FF4444')
ax.set_title('3月26日 申万行业板块涨幅TOP5 — 折线图', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('涨幅 (%)', fontsize=12)
ax.set_ylim(0, 5.5)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_01_line.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 折线图 saved')

# ============================================================
# 2. 柱状图
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(names, changes, color=colors, edgecolor='white', linewidth=1.5, width=0.6)
for bar, c in zip(bars, changes):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f'+{c}%',
            ha='center', va='bottom', fontsize=11, fontweight='bold', color='#333')
ax.set_title('3月26日 申万行业板块涨幅TOP5 — 柱状图', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('涨幅 (%)', fontsize=12)
ax.set_ylim(0, 5.5)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_02_bar.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 柱状图 saved')

# ============================================================
# 3. 饼图
# ============================================================
fig, ax = plt.subplots(figsize=(9, 7))
wedges, texts, autotexts = ax.pie(
    changes, labels=names, colors=colors,
    autopct='%1.1f%%', startangle=140,
    pctdistance=0.75, labeldistance=1.1,
    wedgeprops=dict(edgecolor='white', linewidth=2),
    explode=[0.05]*5
)
for t in texts: t.set_fontsize(11)
for at in autotexts: at.set_fontsize(10); at.set_fontweight('bold')
ax.set_title('3月26日 申万行业板块涨幅TOP5 — 饼图\n（各板块涨幅占比）', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_03_pie.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 饼图 saved')

# ============================================================
# 4. 散点图
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(indices, changes, s=[c*200 for c in changes], c=colors, edgecolors='white', linewidth=2, zorder=5)
for i, (n, idx, c) in enumerate(zip(names, indices, changes)):
    ax.annotate(n, (idx, c), textcoords='offset points', xytext=(8, 5), fontsize=10, color='#333')
ax.set_title('3月26日 申万行业板块 — 散点图\n（X轴:指数点位  Y轴:涨幅  气泡大小:涨幅）', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('板块指数点位', fontsize=12)
ax.set_ylabel('涨幅 (%)', fontsize=12)
ax.grid(linestyle='--', alpha=0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_04_scatter.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 散点图 saved')

# ============================================================
# 5. 热力图
# ============================================================
fig, ax = plt.subplots(figsize=(10, 5))
data_matrix = np.array([[c] for c in changes]).T
im = ax.imshow(data_matrix, cmap='YlOrRd', aspect='auto', vmin=0, vmax=5)
ax.set_xticks(range(len(names)))
ax.set_xticklabels(names, fontsize=12)
ax.set_yticks([0])
ax.set_yticklabels(['涨幅%'], fontsize=12)
for j, c in enumerate(changes):
    ax.text(j, 0, f'+{c}%', ha='center', va='center', fontsize=13, fontweight='bold', color='#333')
plt.colorbar(im, ax=ax, label='涨幅 (%)', shrink=0.8)
ax.set_title('3月26日 申万行业板块涨幅TOP5 — 热力图', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_05_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 热力图 saved')

# ============================================================
# 6. 雷达图
# ============================================================
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
N = len(names)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
values = changes + [changes[0]]
angles += angles[:1]
ax.plot(angles, values, 'o-', linewidth=2.5, color='#FF4444')
ax.fill(angles, values, alpha=0.25, color='#FF4444')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(names, fontsize=11)
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1%', '2%', '3%', '4%', '5%'], fontsize=9, color='gray')
ax.grid(color='gray', linestyle='--', alpha=0.5)
ax.set_title('3月26日 申万行业板块涨幅TOP5 — 雷达图', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_06_radar.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 雷达图 saved')

# ============================================================
# 7. 漏斗图
# ============================================================
fig, ax = plt.subplots(figsize=(9, 7))
bar_heights = 0.6
y_positions = range(len(names)-1, -1, -1)
max_change = max(changes)
for i, (y, name, change, color) in enumerate(zip(y_positions, names, changes, colors)):
    width = change / max_change
    left = (1 - width) / 2
    ax.barh(y, width, left=left, height=bar_heights, color=color, edgecolor='white', linewidth=2)
    ax.text(0.5, y, f'{name}  +{change}%', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
ax.set_xlim(0, 1)
ax.set_ylim(-0.5, len(names)-0.5)
ax.axis('off')
ax.set_title('3月26日 申万行业板块涨幅TOP5 — 漏斗图', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_07_funnel.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 漏斗图 saved')

# ============================================================
# 8. 桑基图（用 matplotlib 模拟）
# ============================================================
fig, ax = plt.subplots(figsize=(12, 7))
total = sum(changes)
left_y = 0.1
right_positions = []
right_y = 0.05
gap = 0.02
for i, (name, change, color) in enumerate(zip(names, changes, colors)):
    h = change / total * 0.8
    right_positions.append((right_y, h))
    right_y += h + gap

left_y = 0.1
for i, (name, change, color) in enumerate(zip(names, changes, colors)):
    h = change / total * 0.8
    ry, rh = right_positions[i]
    # 左侧矩形
    ax.add_patch(mpatches.FancyBboxPatch((0.05, left_y), 0.15, h, boxstyle='round,pad=0.01', color=color, alpha=0.9))
    ax.text(0.125, left_y + h/2, f'A股市场', ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    # 右侧矩形
    ax.add_patch(mpatches.FancyBboxPatch((0.75, ry), 0.15, rh, boxstyle='round,pad=0.01', color=color, alpha=0.9))
    ax.text(0.825, ry + rh/2, f'{name}\n+{change}%', ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    # 连接带
    from matplotlib.patches import PathPatch
    from matplotlib.path import Path
    verts = [(0.20, left_y), (0.50, ry), (0.50, ry+rh), (0.20, left_y+h), (0.20, left_y)]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CLOSEPOLY]
    # 简化为直线连接
    ax.fill([0.20, 0.75, 0.75, 0.20], [left_y, ry, ry+rh, left_y+h], color=color, alpha=0.3)
    left_y += h

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('3月26日 申万行业板块涨幅TOP5 — 桑基图\n（资金流向示意）', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_08_sankey.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 桑基图 saved')

# ============================================================
# 9. K线图（蜡烛图）—— 模拟5个板块当日K线
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
np.random.seed(42)
for i, (name, change, color) in enumerate(zip(names, changes, colors)):
    base = 100
    open_p = base * (1 + np.random.uniform(-0.005, 0.005))
    close_p = open_p * (1 + change/100)
    high_p = max(open_p, close_p) * (1 + np.random.uniform(0.002, 0.008))
    low_p = min(open_p, close_p) * (1 - np.random.uniform(0.002, 0.008))
    # 蜡烛体
    ax.bar(i, abs(close_p - open_p), bottom=min(open_p, close_p), width=0.5, color='#FF4444', edgecolor='#CC0000', linewidth=1.5)
    # 上下影线
    ax.plot([i, i], [low_p, min(open_p, close_p)], color='#CC0000', linewidth=1.5)
    ax.plot([i, i], [max(open_p, close_p), high_p], color='#CC0000', linewidth=1.5)
    ax.text(i, low_p - 0.3, f'+{change}%', ha='center', va='top', fontsize=10, color='#FF4444', fontweight='bold')

ax.set_xticks(range(len(names)))
ax.set_xticklabels(names, fontsize=11)
ax.set_title('3月26日 申万行业板块涨幅TOP5 — K线图（蜡烛图）', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('指数（标准化至100）', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_09_candlestick.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ K线图 saved')

# ============================================================
# 10. 面积图
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(names))
ax.fill_between(x, changes, alpha=0.6, color='#FF4444', label='涨幅')
ax.plot(x, changes, 'o-', color='#CC0000', linewidth=2.5, markersize=9)
for i, (n, c) in enumerate(zip(names, changes)):
    ax.annotate(f'+{c}%', (i, c), textcoords='offset points', xytext=(0, 10), ha='center', fontsize=11, fontweight='bold', color='#CC0000')
ax.set_xticks(x)
ax.set_xticklabels(names, fontsize=11)
ax.set_title('3月26日 申万行业板块涨幅TOP5 — 面积图', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('涨幅 (%)', fontsize=12)
ax.set_ylim(0, 5.5)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_10_area.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 面积图 saved')

# ============================================================
# 11. 气泡图
# ============================================================
fig, ax = plt.subplots(figsize=(10, 7))
for i, (name, change, idx, color) in enumerate(zip(names, changes, indices, colors)):
    size = (change / max(changes)) * 3000
    ax.scatter(i, change, s=size, c=color, alpha=0.8, edgecolors='white', linewidth=2, zorder=5)
    ax.text(i, change, f'+{change}%', ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    ax.text(i, change - 0.55, name, ha='center', va='top', fontsize=10, color='#333')

ax.set_xticks([])
ax.set_title('3月26日 申万行业板块涨幅TOP5 — 气泡图\n（气泡大小代表涨幅大小）', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('涨幅 (%)', fontsize=12)
ax.set_xlim(-0.8, len(names)-0.2)
ax.set_ylim(0.5, 5.5)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/chart_11_bubble.png', dpi=150, bbox_inches='tight')
plt.close()
print('✅ 气泡图 saved')

print('\n🎉 全部11张图表生成完毕！')
