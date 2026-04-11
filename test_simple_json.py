# -*- coding: utf-8 -*-
"""Deep debug JSON serialization"""
import json

# Create simple test data
data = {
    "2026-04-10": {
        "date": "2026-04-10",
        "all_news": [{"title": "test"}],
        "sangsha_module": {"test": "sangsha_0410"}
    },
    "2026-04-09": {
        "date": "2026-04-09", 
        "all_news": [{"title": "test2"}],
        "sangsha_module": {"test": "sangsha_0409"}
    }
}

json_str = json.dumps(data, ensure_ascii=False, indent=2)
print("JSON output:")
print(json_str)
print()

# Check positions
idx_0410 = json_str.find('"2026-04-10"')
idx_0409 = json_str.find('"2026-04-09"')
idx_sg = json_str.find('"sangsha_module"')

print(f'2026-04-10 at: {idx_0410}')
print(f'2026-04-09 at: {idx_0409}')
print(f'First sangsha_module at: {idx_sg}')

# Check which date the first sangsha_module belongs to
if idx_0409 > idx_sg > idx_0410:
    print('First sangsha_module is in 2026-04-10 section')
elif idx_sg > idx_0409:
    print('First sangsha_module is in 2026-04-09 section')
else:
    print('Unexpected position')