import pandas as pd
df=pd.read_csv("data.csv")
print(df)
# Basic Inspection
print(df.head())
print(df.info())
#Missing values check
print(df.isnull().sum())
# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# Check again
print(df.isnull().sum())
# Filter data
filtered = df[df["Age"] > 25]
print(filtered)
# Grouping
grouped = df.groupby("Department")["Salary"].mean()
print(grouped)
# Extra insights
print("Max Salary:", df["Salary"].max())
print("Most common department:", df["Department"].mode()[0])













