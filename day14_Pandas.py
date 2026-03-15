# import pandas as pd

# # Step 1: Read CSV file
# df = pd.read_csv("attendance.csv")

# # Step 2: Calculate attendance percentage
# df["AttendancePercent"] = (
#     df["AttendedClasses"] / df["TotalClasses"]
# ) * 100

# # Step 3: Round percentage
# df["AttendancePercent"] = df["AttendancePercent"].round(2)

# # Step 4: Add warning column (if < 75%)
# df["Status"] = df["AttendancePercent"].apply(
#     lambda x: "Warning" if x < 75 else "Good"
# )

# # Step 5L Save to new file
# df.to_csv("attendance_report.csv", index=False)

# print("Attendance report created successfully!")
# print("Total students:", len(df))
# print("Average attendance:", round(df["AttendancePercent"].mean(), 2))
# print("Highest attendance:", df["AttendancePercent"].max())
# print("Lowest attendance:", df["AttendancePercent"].min())

# sorted_df = df.sort_values(by="AttendancePercent", ascending=False)
# print("Sorted (desc):\n", sorted_df)

# print("\nTop 2:\n", sorted_df.head(2))



#######################################################################################################


# - Read sales.csv
# - Create Revenue = Qty * UnitPrice
# - Find:
#   Total Revenue (sum)
#   Top product by Revenue (max)
# - Save output to sales_report.csv


import pandas as pd

df = pd.read_csv("sales.csv")
df["Revenue"] = (df["Qty"] * df["UnitPrice"])

total_revenue = df["Revenue"].sum()
print("Total Revenue:", total_revenue)

max_revenue = df["Revenue"].max()
print("Top Revenue:", max_revenue)

df.to_csv("sales_report.csv", index=False)
print("Report saved as sales_report.csv")

