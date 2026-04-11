# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('news_data/news_2026-04-11.json', encoding='utf-8') as f:
    data = json.load(f)

# 悟空对各新闻的判断（用于生成 bayes_analysis）
# 这些值来自悟空分析 + 八戒贝叶斯逻辑
bayes_data = {
    # ========== S级 ==========
    "美伊谈判正式举行": {
        "prior_judgment": "地缘风险已部分定价，市场预期温和",
        "prior_prob": 55,
        "likelihood_judgment": "三国代表同出席=谈判级别史上最高，缓和预期升温；但双方分歧明确，达成协议概率低",
        "likelihood_prob": 62,
        "posterior": 58,
        "expected_return": "黄金/原油-1%~+1%，取决于谈判进展",
        "confidence_interval": "[-2%, +3%]",
        "key_variables": "谈判是否破裂、Trump是否追加制裁、霍尔木兹管控权"
    },
    "俄乌敖德萨遭袭": {
        "prior_judgment": "美伊谈判压制避险情绪",
        "prior_prob": 52,
        "likelihood_judgment": "俄乌升温=地缘风险分散Trump精力，对伊谈判更迫切；整体避险逻辑混沌",
        "likelihood_prob": 48,
        "posterior": 50,
        "expected_return": "黄金/原油震荡，+0%~+2%",
        "confidence_interval": "[-1.5%, +3%]",
        "key_variables": "俄乌冲突是否扩大、美伊谈判进展"
    },
    "美国释放SPR": {
        "prior_judgment": "SPR释放=打压油价",
        "prior_prob": 45,
        "likelihood_judgment": "848万桶是小规模试探，不影响中长期供需；市场已预期对伊制裁解除",
        "likelihood_prob": 58,
        "posterior": 52,
        "expected_return": "原油-0.5%~+0.5%，短期冲击有限",
        "confidence_interval": "[-1%, +1.5%]",
        "key_variables": "OPEC+是否减产对冲、伊朗产能恢复速度"
    },
    # ========== A级 ==========
    "华为/地平线/蔚来": {
        "prior_judgment": "自动驾驶板块估值偏高，利好已部分反映",
        "prior_prob": 58,
        "likelihood_judgment": "四巨头同日发声=行业共识确立，2026年L3量产是实质性催化；主机厂+芯片+软件全产业链共振",
        "likelihood_prob": 72,
        "posterior": 68,
        "expected_return": "AI算力ETF+3%~+8%，智能驾驶板块+5%~+12%",
        "confidence_interval": "[+1%, +15%]",
        "key_variables": "政策L3准入时间表、芯片算力突破、OEM量产节奏"
    },
    "闪迪跻身纳指100": {
        "prior_judgment": "AI存储板块已强势，2500%涨幅已充分定价",
        "prior_prob": 55,
        "likelihood_judgment": "闪迪被纳指100纳入=被动资金买入+机构背书，短期还有上涨惯性；但2500%涨幅已是超级泡沫信号",
        "likelihood_prob": 65,
        "posterior": 63,
        "expected_return": "AI存储个股短期+5%~+15%，中期风险收益比差",
        "confidence_interval": "[+2%, +20%]",
        "key_variables": "纳指100调仓日资金流向、AI存储需求是否持续、竞争对手动态"
    },
    "变压器出口": {
        "prior_judgment": "电网设备板块平稳，订单可见性低",
        "prior_prob": 50,
        "likelihood_judgment": "变压器出口+十五五电网招标=订单可见性提升，电网投资上行周期确立；但A股电网标的估值已较高",
        "likelihood_prob": 62,
        "posterior": 58,
        "expected_return": "电网ETF+2%~+6%",
        "confidence_interval": "[+0.5%, +8%]",
        "key_variables": "南瑞/许继/平高订单兑现情况、电网投资计划金额"
    },
}

def add_bayes(news_list):
    count = 0
    for item in news_list:
        title = item.get('title', '')
        for key, bayes in bayes_data.items():
            if key in title:
                item['bayes_analysis'] = bayes.copy()
                count += 1
                break
    return count

sl_count = add_bayes(data.get('s_level', []))
al_count = add_bayes(data.get('a_level', []))
dy_count = add_bayes(data.get('douyin', []))

print("S级加bayes: %d条" % sl_count)
print("A级加bayes: %d条" % al_count)
print("抖音加bayes: %d条" % dy_count)

with open('news_data/news_2026-04-11.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("已写回 news_2026-04-11.json")

# 验证
with open('news_data/news_2026-04-11.json', encoding='utf-8') as f:
    verify = json.load(f)
sl = verify.get('s_level', [])
al = verify.get('a_level', [])
print("\n=== 验证 bayes_analysis ===")
for i, item in enumerate(sl):
    has = 'bayes_analysis' in item
    print("S[%d] %s: %s" % (i, item.get('title','')[:30], "有" if has else "无"))
for i, item in enumerate(al):
    has = 'bayes_analysis' in item
    print("A[%d] %s: %s" % (i, item.get('title','')[:30], "有" if has else "无"))
