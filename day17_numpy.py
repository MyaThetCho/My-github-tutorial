import numpy as np


# numbers = np.array([10,20,30,40])
# print(numbers)


a = [10,20,30]
a = np.array([10,20,30])
print(a+5)


# # Basic NumPy Functions
# a.sum()
# a.mean()
# a.max()
# a.min()


# 2D Array (Martix)
marks = np.array([
    [80, 75, 90],
    [60, 65, 70],
    [85, 88, 92]
    ])
print(marks)

 # Axis Concept (Very Important)
 # Column total
print(marks.sum(axis=0))

# Row total
print(marks.sum(axis=1))


marks = np.array([80, 90, 75, 60, 85])
print("Average:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())

