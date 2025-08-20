
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "temp_c": [10, 22, 5, 30, 12, 18, 8, 25],
    "rain": [1, 0, 1, 0, 1, 0, 1, 0],
    "wind": [20, 10, 40, 5, 15, 12, 30, 5],
    "mont": [1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
X = df[["temp_c", "rain", "wind"]]
y = df["mont"]

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X, y)

examples = pd.DataFrame([
    {"temp_c": 12, "rain": 1, "wind": 20},
    {"temp_c": 25, "rain": 0, "wind": 5},
    {"temp_c": 8,  "rain": 0, "wind": 40},
])

for i, row in examples.iterrows():
    tahmin = "Mont Giy" if model.predict(pd.DataFrame([row]))[0] == 1 else "Mont Gerek Yok"
    print(f"Örnek {i+1} → Tahmin: {tahmin}")
