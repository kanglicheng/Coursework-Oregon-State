import pandas as pd

# Step 2: Read the data
df = pd.read_csv('hw1-data/income.train.5k.csv', header=0)

print(df['age'].describe())
print(df['hours'].describe())
print(pd.get_dummies(df), 'dfd')

# Step 3: Count the total number of rows
total_rows = len(df)
print(total_rows)
print(df.columns)
# print(df.head())

# Step 4: Filter the rows with a positive label
positive_label_rows = df[df["target"] == ">50K"]

# Step 5: Count the number of rows with a positive label
positive_count = len(positive_label_rows)

# Step 6: Calculate the percentage
positive_percentage = (positive_count / total_rows) * 100

# Step 7: Print the result
print(f"Percentage of data with a positive label: {positive_percentage:.2f}%")
# Output: Percentage of data with a positive label: 25.03%


print(df['age'].describe()) # max age is 90, min age is 17

print(max(df['hours']), min(df['hours'])) # max hours is 99, min hours is 1