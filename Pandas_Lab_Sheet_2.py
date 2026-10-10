import pandas as pd

# Create DataFrame
data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Puja", "Rahul", "Nidhi", "Palak", "Abdul", "Aman", "Neha", "Riya"],
    "Department": ["BCA", "BCA", "MCA", "BBA", "MCA", "BCA", "BBA", "MCA"],
    "Age": [20, 22, 23, 21, 24, 20, 22, 23],
    "Marks": [85, 78, 92, 68, 88, 35, 75, 95]
}

df = pd.DataFrame(data)

# LEVEL 1 - BASIC

# Q1. Display complete DataFrame
print("\nQ1. Complete DataFrame")
print(df)

# Q2. Display first 3 records
print("\nQ2. First 3 records")
print(df.head(3))

# Q3. Display last 2 records
print("\nQ3. Last 2 records")
print(df.tail(2))

# Q4. Number of rows and columns
print("\nQ4. Rows and Columns")
print(df.shape)

# Q5. Display column names
print("\nQ5. Column Names")
print(df.columns)

# Q6. Display data types
print("\nQ6. Data Types")
print(df.dtypes)

# Q7. Display Name column
print("\nQ7. Name Column")
print(df["Name"])

# Q8. Display Name and Marks
print("\nQ8. Name and Marks")
print(df[["Name", "Marks"]])


# LEVEL 2 - SELECTION AND FILTERING

# Q9. Students scoring more than 80
print("\nQ9. Marks Greater Than 80")
print(df[df["Marks"] > 80])

# Q10. Students scoring less than 70
print("\nQ10. Marks Less Than 70")
print(df[df["Marks"] < 70])

# Q11. Marks between 70 and 90
print("\nQ11. Marks Between 70 and 90")
print(df[df["Marks"].between(70, 90)])

# Q12. BCA students
print("\nQ12. BCA Students")
print(df[df["Department"] == "BCA"])

# Q13. MCA students scoring more than 80
print("\nQ13. MCA Students Scoring Above 80")
print(df[(df["Department"] == "MCA") & (df["Marks"] > 80)])

# Q14. Students older than 21
print("\nQ14. Age Greater Than 21")
print(df[df["Age"] > 21])


# LEVEL 3 - DATA ANALYSIS

# Q15. Average marks
print("\nQ15. Average Marks")
print(df["Marks"].mean())

# Q16. Maximum marks
print("\nQ16. Maximum Marks")
print(df["Marks"].max())

# Q17. Minimum marks
print("\nQ17. Minimum Marks")
print(df["Marks"].min())

# Q18. Median marks
print("\nQ18. Median Marks")
print(df["Marks"].median())

# Q19. Count students scoring above 75
print("\nQ19. Students Scoring Above 75")
print((df["Marks"] > 75).sum())

# Q20. Average marks of BCA students
print("\nQ20. Average Marks of BCA Students")
print(df[df["Department"] == "BCA"]["Marks"].mean())

# Q21. Average marks of MCA students
print("\nQ21. Average Marks of MCA Students")
print(df[df["Department"] == "MCA"]["Marks"].mean())

# Q22. Highest-scoring student
print("\nQ22. Highest-Scoring Student")
print(df.loc[df["Marks"].idxmax()])


# LEVEL 4 - DATA MANIPULATION

# Q23. Add Bonus column
df["Bonus"] = 5
print("\nQ23. Bonus Column Added")
print(df)

# Q24. Create FinalMarks column
df["FinalMarks"] = df["Marks"] + df["Bonus"]
print("\nQ24. Final Marks")
print(df[["Name", "Marks", "Bonus", "FinalMarks"]])

# Q25. Create Result column
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)
print("\nQ25. Result Column")
print(df[["Name", "Marks", "Result"]])

# Q26. Create Grade column
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Marks"].apply(grade)
print("\nQ26. Grade Column")
print(df[["Name", "Marks", "Grade"]])


# LEVEL 5 - RANKING

# Q27. Sort students by marks descending
print("\nQ27. Students Sorted by Marks")
print(df.sort_values("Marks", ascending=False))

# Q28. Display top 3 students
print("\nQ28. Top 3 Students")
print(df.nlargest(3, "Marks"))

# Q29. Add Rank column
df["Rank"] = df["Marks"].rank(
    ascending=False, method="min"
).astype(int)
print("\nQ29. Rank Column")
print(df[["Rank", "Name", "Marks"]].sort_values("Rank"))


# LEVEL 6 - GROUP ANALYSIS

# Q30. Number of students in each department
print("\nQ30. Students in Each Department")
print(df.groupby("Department")["Name"].count())

# Q31. Average marks of each department
print("\nQ31. Average Marks by Department")
print(df.groupby("Department")["Marks"].mean())

# Q32. Maximum marks in each department
print("\nQ32. Maximum Marks by Department")
print(df.groupby("Department")["Marks"].max())

# Q33. Minimum marks in each department
print("\nQ33. Minimum Marks by Department")
print(df.groupby("Department")["Marks"].min())

# Combined group analysis
print("\nCombined Group Analysis")
print(
    df.groupby("Department")["Marks"].agg(
        ["count", "mean", "max", "min"]
    )
)


# CHALLENGE QUESTION - FINAL MERIT LIST

# Create final merit list
merit_list = df[
    ["Rank", "RollNo", "Name", "Department",
     "Marks", "Grade", "Result"]
].sort_values("Marks", ascending=False)

print("\nFINAL MERIT LIST")
print(merit_list)

# Export merit list to Excel
merit_list.to_excel("student_merit_list.xlsx", index=False)

print("\nMerit list exported successfully!")
