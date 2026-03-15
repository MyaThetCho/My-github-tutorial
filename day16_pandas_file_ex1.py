import pandas as pd


'''
Exercise 1: Convert CSV to excel
Read students.csv
Display first rows
Save data to students.xlsx
'''
# df = pd.read_csv("students.csv")
# print(df.head())
# df.to_excel("students.xlsx", index=False)
# print("Excel file created")




'''
Exercise 2: Excel File Analysis
Read students.xlsx
Calculate: Average, Highest, Lowest
'''
# df = pd.read_excel("students.xlsx")
# print("Average Marks:", df["Marks"].mean().round(2))
# print("Highest Marks:", df["Marks"].max())
# print("Lowest Marks:", df["Marks"].min())




'''
Exercise 3: Add New Column
Read students.xlsx
Create column Grade
Save to report.xlsx
'''
# df = pd.read_excel("students.xlsx")
# df["Grade"] = df["Marks"].apply(lambda x: "Good" if x>=80 else "Average")
# df.to_excel("report.xlsx", index=False)
# print(df)



'''
Exercise 4: Sales Revenue(CSV)
Read sales.csv
Calculate Revenue = Qty * Price
Find Total Revenue
Save report
'''
# df = pd.read_csv("sales1.csv")
# df["Revenue"] = df["Qty"] * df["Price"]
# print("Total Revenue:", df["Revenue"].sum())
# df.to_excel("sales_report.xlsx", index=False)



'''
Exercise 5: Filter Data
Show only students with marks greater than 80.
'''
# df = pd.read_excel("students.xlsx")
# high_marks = df[df["Marks"]>80]
# print(high_marks)



'''
Exercise 6: Sorting
Sort students by marks highest first.
'''
# df = pd.read_excel("students.xlsx")
# sorted_df = df.sort_values(by="Marks", ascending=False)
# print(sorted_df)



'''
Exercise 7: Top Student
Find the stuend with highest marks.
'''
# df = pd.read_excel("students.xlsx")
# top = df[df["Marks"] == df["Marks"].max()]
# print("Top Student:")
# print(top)


