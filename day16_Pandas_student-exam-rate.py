import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("student_marks.csv")

df["Total"] = df["Math"] + df["English"] + df["Science"]
df["Average"] = (df["Total"] / 3).round(2)

conditions = [
    df["Average"] >= 80,
    (df["Average"] >= 70) & (df["Average"] < 80),
    (df["Average"] >= 50) & (df["Average"] < 70),
    df["Average"] < 50
]

results = ["Distinction", "Merit", "Pass", "Fail"]
df["Result"] = np.select(conditions, results, default="Fail")
print(df)

count = df["Result"].value_counts()

count.plot(kind="pie", autopct="%1.1f%%", startangle = 90)

plt.title("Student Result Distribution")
plt.ylabel("")
plt.show()
