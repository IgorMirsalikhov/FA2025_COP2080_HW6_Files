import json
from fractions import Fraction

def fraction_decoder(obj):
    pass

# === TEST CODE ===
with open("fractions.json", "r") as f:
    loaded_data = json.load(f, object_hook=fraction_decoder)

data = loaded_data.get("questions", 0)
for d in data:
    print(d.get("value", 0))

