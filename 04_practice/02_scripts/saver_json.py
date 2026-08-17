import json
from pathlib import Path

shop = ["milk", "bread", "eggs"]
path = Path("data")
path.mkdir(exist_ok=True)
with open(path / "shop.json", "w", encoding="utf-8") as f:
    json.dump(shop, f, ensure_ascii=False, indent=2)

with open(path / "shop.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
print(loaded == shop)
