# import numpy as np

# students = np.array(["Aung", "Mya", "Kyaw", "Su", "Hla"])

# marks = np.array([
#     [80, 75, 90],
#     [60, 65, 70],
#     [45, 50, 40],
#     [85, 88, 92],
#     [70, 72, 68]
# ])

# total_marks = marks.sum(axis=1)

# average_marks = marks.mean(axis=1)

# highest_total = total_marks.max()
# lowest_total = total_marks.min()

# result = np.where(average_marks >= 50, "Pass", "Fail") 

# subject_average = marks.mean(axis=0)

# grade = np.where(average_marks >= 80, "Distinction",
#         np.where(average_marks >= 70, "Merit",
#         np.where(average_marks >= 50, "Pass", "Fail")))

# print("Student Result Report")
# print("-" * 40)

# for i in range(len(students)):
#     print("Name:", students[i])
#     print("Total:", total_marks[i])
#     print("Average:", round(average_marks[i], 2))
#     print("Result:", result[i])
#     print("Grade:", grade[i])
#     print("-" * 40)
    
# print("Highest Total:", highest_total)
# print("Lowest Total:", lowest_total)

# print("Subject Averages:")
# print("Math:", round(subject_average[0], 2))
# print("English:", round(subject_average[1], 2))
# print("Science:", round(subject_average[2], 2))




##############################################################################################################





import numpy as np
students = np.array(["Aung", "Mya", "Kyaw", "Su"])
total = np.array([240,200,260,220])

top_index = total.argmax()
print("Top student:", students[top_index])

low_index = total.argmin()
print("Lowest student:", students[low_index])

rank_index = total.argsort()
print("Ranking order:", students[rank_index])

print("Ranking order:", students[total.argsort()[::-1]])

marks = np.array([80,60,95,70])
print(marks.argmin())
print(marks.argsort())

