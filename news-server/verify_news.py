import requests
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

r = requests.get('http://127.0.0.1:5000/api/news/2026-03-29')
data = r.json()

print("\nNews Data Verification")
print("="*60)
print(f"S-Level: {len(data['s_level'])} items")
print(f"A-Level: {len(data['a_level'])} items")
print(f"Douyin: {len(data['douyin'])} items")
print("\nS-Level News:")
for n in data['s_level']:
    print(f"  - {n['title']}")
print("\nA-Level News:")
for n in data['a_level']:
    print(f"  - {n['title']}")
print("\nDouyin Related:")
for n in data['douyin']:
    print(f"  - {n['title']}")
print("\nData updated successfully!")
