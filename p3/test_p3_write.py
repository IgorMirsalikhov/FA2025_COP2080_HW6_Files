import json
from fractions import Fraction

class FractionEncoder(json.JSONEncoder):
    pass

# === TEST CODE ===
data = {
    "questions": [
        {"id": 1, "value": Fraction(3, 4)},
        {"id": 2, "value": Fraction(2, 6)},
        {"id": 3, "value": Fraction(-5, -10)}
    ],
    "answer": Fraction(5, 8)
}

with open("fractions.json", "w") as f:
    json.dump(data, f, indent=4, cls=FractionEncoder)

print(f"Success! Data is saved in {f.name}")
