import pandas as pd

data = pd.read_csv("data/gender-gap-in-average-wages-ilo.csv")
print(data.head())  # Displays the first few rows of the dataset
print(data.columns)  # Lists all column names

pivot_data = data.pivot(index='Year', columns='Entity', values='Gender wage gap (%)')
