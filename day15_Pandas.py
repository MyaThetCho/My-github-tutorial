# Pandas has two important structure
# Series, One column of data
# DataFrame, Table of rows and colums

import pandas as pd

# # A Series is like a single column
# marks = pd.Series([80,75,90,60])
# print(marks)


# A DataFrame is like an Excel table.
data = {
    "Name": ["Aung", "Mya", "Kyaw", "Ko", "Su", "Ni", "Mg"],
    "Marks": [80,90,75,78,87,86,97]
}
df = pd.DataFrame(data)
# print(df)

# shows the first 5 rows of the DataFrame
# print(df.head())   # Display first 5 rows
# print(df.head(2))

# print(df.tail())   # Display last 5 rows
# print(df.tail(2))

# print(df.shape)      # rows and columns
# print(df.columns)    # column names
# print(df.info())     # data information


# print(df["Marks"])

# # Basic Calculations
# print(df["Marks"].mean().round(2)) #mean
# print(df["Marks"].max())
# print(df["Marks"].min())
# print(df["Marks"].sum())

#######################################################################

# df = pd.read_csv("students.csv")
# print(df)

# df.to_csv("output.csv", index = False)

#####################################################################

df = pd.read_csv("sales1.csv")
df["Revenue"] = df["Qty"] * df["Price"]
print("Total Revenue:", df["Revenue"].sum())
print("Highest Revenue:", df["Revenue"].max())


