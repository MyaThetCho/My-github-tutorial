import numpy as np
marks = np.array([80,60,95,70,85])
names = ["Aung", "Mya", "Kyaw", "Su", "Hla"]


import pandas as pd
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})
print(df)

print("Average:", df["Marks"].mean())
print("Top student:")
print(df[df["Marks"]==df["Marks"].max()])


import matplotlib.pyplot as plt
students = ["Aung", "Mya", "Kyaw", "Su", "Hla"]
marks = np.array([80,60,95,70,85])
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


plt.hist(marks)
plt.title("Marks Distribution")
plt.show()








