import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('insights.json', encoding='utf-8') as f:
    d = json.load(f)

# Fix etf_knowledge
d['etf_knowledge'] = [
    {
        "id": "ETF-KW-001",
        "wrong_code": "159542",
        "wrong_name": "电网ETF",
        "correct_code": "159320",
        "correct_name": "电网ETF",
        "category": "power_grid",
        "confirmed_date": "2026-04-11",
        "root_cause": "159542是机械ETF，159320才是电网ETF（特高压/变压器/硅钢/十五五）。注：159320不在1386只ETF官方列表中，可能是近期新发"
    },
    {
        "id": "ETF-KW-002",
        "wrong_code": "159871",
        "wrong_name": "新能源电池ETF",
        "correct_code": "516070",
        "correct_name": "易方达新能源ETF",
        "category": "new_energy",
        "confirmed_date": "2026-04-10",
        "root_cause": "159871不是电池ETF；易方达新能源ETF(516070)才是新能源+自动驾驶主题的正确代码"
    },
    {
        "id": "ETF-KW-003",
        "wrong_code": "512880",
        "wrong_name": "银行ETF / 国债ETF / 证券ETF",
        "correct_code": "512880",
        "correct_name": "证券ETF",
        "category": "securities",
        "confirmed_date": "2026-04-12",
        "root_cause": "512880=证券ETF（券商/中信证券），银行=512800，国债=无，酒=512690，石油=561360，切勿混淆"
    },
    {
        "id": "ETF-KW-004",
        "wrong_code": "512690",
        "wrong_name": "金融ETF / 能源ETF",
        "correct_code": "512690",
        "correct_name": "酒ETF",
        "category": "liquor",
        "confirmed_date": "2026-04-12",
        "root_cause": "512690=酒ETF（白酒/茅台/五粮液），不是能源ETF(石油/电力)，也不是金融ETF"
    },
    {
        "id": "ETF-KW-005",
        "wrong_code": "159322",
        "wrong_name": "黄金股ETF平安",
        "correct_code": "待核查",
        "correct_name": "不在1386只ETF官方列表中",
        "category": "unknown",
        "confirmed_date": "2026-04-12",
        "root_cause": "159322未出现在用户提供ETF列表中，可能是基金专户/LOF等边缘产品"
    },
    {
        "id": "ETF-KW-006",
        "wrong_code": "515220",
        "wrong_name": "电力ETF",
        "correct_code": "561700",
        "correct_name": "电力ETF博时",
        "category": "power",
        "confirmed_date": "2026-04-12",
        "root_cause": "515220=煤炭ETF（非电力），电力ETF是561700，清洁能源/电网=159320电网ETF"
    },
    {
        "id": "ETF-KW-007",
        "wrong_code": "512800",
        "wrong_name": "金融ETF",
        "correct_code": "512800",
        "correct_name": "银行ETF",
        "category": "bank",
        "confirmed_date": "2026-04-12",
        "root_cause": "512800=银行ETF（工行/招行/六大行），金融综合=512800银行+512900证券+512070保险，不要混用"
    },
    {
        "id": "ETF-KW-008",
        "wrong_code": "512880",
        "wrong_name": "国债ETF / 银行ETF",
        "correct_code": "512880",
        "correct_name": "证券ETF",
        "category": "securities",
        "confirmed_date": "2026-04-12",
        "root_cause": "512880=证券ETF（券商/中信证券），新闻提到券商/证券/中信证券时必须用512900"
    }
]

# Fix ETF-001 pattern
for i, p in enumerate(d['patterns']):
    if p.get('id') == 'ETF-001':
        d['patterns'][i] = {
            "id": "ETF-001",
            "name": "ETF code/name mapping — must verify before citing (v2.0)",
            "category": "etf_knowledge",
            "confidence": 95,
            "status": "active",
            "verified_count": 8,
            "source": "2026-04-12 comprehensive audit + 全市场ETF列表(v2.0)",
            "formula": "News theme -> check etf_map.json -> use verified code",
            "scope": "All A-share ETF references in financial news analysis",
            "boundaries": "Always use etf_map.json when ANY news mentions ETF code or theme",
            "key_signal": "Any ETF name in analysis",
            "trading_rules": [
                "512880 = 证券ETF（券商/中信证券）≠ 银行ETF(512800) ≠ 国债ETF(无) ≠ 酒ETF(512690)",
                "512800 = 银行ETF（工行/招行/六大行/净息差）≠ 金融ETF",
                "512690 = 酒ETF（白酒/茅台/五粮液）≠ 能源ETF",
                "512900 = 证券ETF（券商/中信证券）— 新闻提到券商/证券就用512900",
                "561360 = 石油ETF（原油/能源）",
                "515220 = 煤炭ETF（非电力）≠ 电力ETF",
                "561700 = 电力ETF博时",
                "159320 = 电网ETF（特高压/变压器/十五五/硅钢）",
                "159755 = 电池ETF（钠锂混合/宁德时代/储能/动力电池）",
                "516070 = 易方达新能源ETF（光伏+锂电+智能汽车）≠ 516160新能源ETF",
                "512480 = 半导体ETF（芯片设备/半导体材料）",
                "512760 = 芯片ETF（AI芯片/存储/美光/铠侠）≠ 512480半导体ETF",
                "588200 = 科创芯片ETF",
                "515070 = 人工智能AIETF",
                "512930 = AI人工智能ETF（算力）",
                "159819 = 人工智能ETF易方达",
                "515980 = 人工智能ETF（云计算/大数据/SpaceX/字节）",
                "518880 = 黄金ETF（避险/地缘/金价）",
                "159985 = 豆粕ETF（农产品/期货/农业）",
                "561360 = 石油ETF",
                "515220 = 煤炭ETF（≠电力ETF）",
                "When news says 银行+券商+保险: use 512800银行ETF + 512900证券ETF + 512070保险ETF separately",
                "NEVER infer ETF code from news thematic keywords alone — always cross-reference etf_map.json first",
                "NEVER write '银行ETF' without confirming code: bank=512800, liquor=512690, securities=512880"
            ],
            "failure_lessons": [
                "Root cause: 512880 wrong = 证券ETF was mistakenly called 国债ETF/银行ETF because of thematic confusion",
                "Root cause: 512690 wrong = 酒ETF was mistakenly called 金融ETF/能源ETF",
                "Root cause: 515220 wrong = 煤炭ETF was called 电力ETF",
                "Root cause: 159542 wrong = 159320电网ETF was replaced with similar-looking code 159542",
                "Prevention: Use etf_map.json as the single source of truth. Never guess codes."
            ]
        }
        print(f'ETF-001 pattern updated at index {i}')
        break

d['last_updated'] = '2026-04-12'

with open('insights.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f'Saved. etf_knowledge: {len(d["etf_knowledge"])} entries')
print('Done.')
