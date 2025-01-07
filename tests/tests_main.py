import matplotlib.pyplot as plt
import seaborn as sns

# Filter only BRICS countries from the final data
brics_final_data = final_brics_g7_data[final_brics_g7_data['Country'].isin(brics_countries)]

# Set the plot style
sns.set(style="whitegrid")

# Create the plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=brics_final_data, x='Year', y='GDP/Capita (PPP)', hue='Country', marker='o')

# Add titles and labels
plt.title("GDP/Capita (PPP) for BRICS Countries (2000-2020)", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("GDP/Capita (PPP)", fontsize=14)
plt.xticks([2000, 2010, 2020], fontsize=12)
plt.legend(title="Country", fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()
