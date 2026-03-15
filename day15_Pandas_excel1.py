# import pandas as pd

# df = pd.read_csv("students.csv")
# df["Grade"] = df["Marks"].apply(lambda x: "Good" if x >= 80 else "Average")
# df.to_excel("output.xlsx", index=False)

#################################################################################################################

'''
Read an Excel file using Pandas
Display the first rows of the data
Calculate the average marks
Find the highest marks
Save the results to a new Excel file
'''

import pandas as pd

df = pd.read_excel("students.xlsx")
print(df.head())
average_marks = round(df["Marks"].mean(),2)
print("Average Marks:", average_marks)

highest_marks = df["Marks"].max()
print("Higheset Marks:", highest_marks)

df.to_excel("students_report.xlsx", index=False)

print("Report saved to students_report.xlsx")
