"""
Pandas 向量化回测脚本 — 大阴线放量止盈策略
============================================
核心思路：
  大阴线 + 放量 + 价格在 MA5 上方 → 买入信号（次日执行）
  纯向量化操作，零循环

运行方式：
  python backtest_vectorized.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────
# 1. 数据准备（演示用随机数据，替换为真实数据即可）
# ──────────────────────────────────────────────
np.random.seed(42)
n = 500
dates = pd.date_range("2025-01-01", periods=n, freq="B")

# 生成模拟行情
close = 100 + np.cumsum(np.random.randn(n) * 2)
open_ = close + np.random.randn(n) * 1.5          # open 偏离 close
high = np.maximum(close, open_) + np.abs(np.random.randn(n))
low = np.minimum(close, open_) - np.abs(np.random.randn(n))
volume = np.random.randint(100_000, 500_000, n).astype(float)

df = pd.DataFrame(
    {"open": open_, "high": high, "low": low, "close": close, "volume": volume},
    index=dates,
)

# ──────────────────────────────────────────────
# 2. 信号生成（全向量化，零循环）
# ──────────────────────────────────────────────

# 2-1  大阴线：收盘 < 开盘
df["is_negative"] = df["close"] < df["open"]

# 2-2  放量：成交量 > 5 日均量 × 2
df["vol_ma5"] = df["volume"].rolling(5).mean()
df["is_volume_surge"] = df["volume"] > df["vol_ma5"] * 2

# 2-3  5 日均线
df["ma5"] = df["close"].rolling(5).mean()

# 2-4  止盈信号：大阴线 & 放量 & 收盘价在 MA5 上方
df["signal"] = (
    df["is_negative"]
    & df["is_volume_surge"]
    & (df["close"] > df["ma5"])
).astype(int)

# ──────────────────────────────────────────────
# 3. 收益率计算（向量化）
# ──────────────────────────────────────────────

# 3-1  每日收益率
df["daily_return"] = df["close"].pct_change()

# 3-2  信号 shift(1) 对齐到次日收益 → 当天信号次日执行
df["strategy_return"] = df["signal"].shift(1) * df["daily_return"]

# 去掉 NaN
df = df.dropna()

# ──────────────────────────────────────────────
# 4. 评估指标
# ──────────────────────────────────────────────

# 累计净值
df["cum_strategy"] = (1 + df["strategy_return"]).cumprod()
df["cum_benchmark"] = (1 + df["daily_return"]).cumprod()

# 累计收益率
cum_return = df["cum_strategy"].iloc[-1] - 1

# 年化收益率
n_days = len(df)
annualized_return = (1 + cum_return) ** (252 / n_days) - 1

# 最大回撤
df["peak"] = df["cum_strategy"].cummax()
df["drawdown"] = (df["cum_strategy"] - df["peak"]) / df["peak"]
max_drawdown = df["drawdown"].min()

# 胜率
trade_returns = df.loc[df["signal"].shift(1) == 1, "daily_return"]
win_rate = (trade_returns > 0).mean() if len(trade_returns) > 0 else 0

# 信号次数
signal_count = df["signal"].sum()

print("=" * 50)
print("[BACKTEST] 回测评估报告")
print("=" * 50)
print(f"  信号触发次数 : {signal_count}")
print(f"  累计收益率   : {cum_return:+.2%}")
print(f"  年化收益率   : {annualized_return:+.2%}")
print(f"  最大回撤     : {max_drawdown:.2%}")
print(f"  交易胜率     : {win_rate:.2%}")
print(f"  基准累计收益 : {df['cum_benchmark'].iloc[-1] - 1:+.2%}")
print("=" * 50)

# ──────────────────────────────────────────────
# 5. 绘图
# ──────────────────────────────────────────────
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False

fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=True,
                         gridspec_kw={"height_ratios": [3, 1.5, 2]})

# ---- 5-1  净值曲线 ----
axes[0].plot(df.index, df["cum_strategy"], label="策略净值", color="#2196F3", linewidth=1.5)
axes[0].plot(df.index, df["cum_benchmark"], label="基准(持有)", color="gray", alpha=0.5, linewidth=1)
axes[0].set_title("大阴线放量止盈策略 — 净值曲线", fontsize=14, fontweight="bold")
axes[0].set_ylabel("累计净值")
axes[0].legend(loc="upper left")
axes[0].grid(True, alpha=0.3)

# ---- 5-2  回撤 ----
axes[1].fill_between(df.index, df["drawdown"], 0, color="#f44336", alpha=0.35)
axes[1].set_title("策略回撤", fontsize=11)
axes[1].set_ylabel("回撤")
axes[1].grid(True, alpha=0.3)

# ---- 5-3  价格 + 信号标记 ----
axes[2].plot(df.index, df["close"], label="收盘价", color="black", alpha=0.7, linewidth=0.8)
axes[2].plot(df.index, df["ma5"], label="MA5", color="orange", alpha=0.5, linewidth=0.8)
signal_dates = df[df["signal"] == 1].index
axes[2].scatter(
    signal_dates, df.loc[signal_dates, "close"],
    color="red", marker="^", s=50, zorder=5, label="买入信号",
)
axes[2].set_title("价格与信号标记", fontsize=11)
axes[2].set_ylabel("价格")
axes[2].legend(loc="upper left")
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("backtest_result.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n[OK] 图表已保存: backtest_result.png")
