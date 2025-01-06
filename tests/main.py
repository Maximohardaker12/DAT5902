import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/gender-gap-in-average-wages-ilo.csv")

data.rename(columns={'Entity': 'Country'}, inplace=True)

print(data.head())

sns.set(style="whitegrid")

pivot_data = data.pivot(index='Year', columns='Country', values='Gender wage gap (%)')

pivot_data.plot(kind='bar', figsize=(12, 8), width=0.8)

plt.title("Gender Pay Gap by Country and Year", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Gender Pay Gap (%)", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.savefig("gender_pay_gap_clustered_bar_chart.png")
plt.show()
