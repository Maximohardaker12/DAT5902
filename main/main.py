import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("data/gdp_per_capita.csv")
data.rename(columns={'Entity': 'Country', 'GDP per capita, PPP (constant 2017 international $)': 'GDP/Capita (PPP)'}, inplace=True)

brics_countries = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
g7_countries = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']

brics_data = data[data['Country'].isin(brics_countries)]
g7_data = data[data['Country'].isin(g7_countries)]

brics_g7_data = pd.concat([brics_data, g7_data])
brics_g7_data.reset_index(drop=True, inplace=True)

print(brics_g7_data)
brics_g7_data['GDP/Capita (PPP)'] = brics_g7_data['GDP/Capita (PPP)'].round(2)
brics_g7_data = brics_g7_data.sort_values(by='GDP/Capita (PPP)', ascending=False)
brics_g7_data_2000 = brics_g7_data[brics_g7_data['Year'] == 2000]
brics_g7_data_2010 = brics_g7_data[brics_g7_data['Year'] == 2010]
brics_g7_data_2020 = brics_g7_data[brics_g7_data['Year'] == 2020]

print(brics_g7_data_2000)
print(brics_g7_data_2010)
print(brics_g7_data_2020)

final_brics_g7_data = pd.concat([brics_g7_data_2000, brics_g7_data_2010, brics_g7_data_2020])
print(final_brics_g7_data)



brics_final_data = final_brics_g7_data[final_brics_g7_data['Country'].isin(brics_countries)]

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=brics_final_data, x='Year', y='GDP/Capita (PPP)', hue='Country', marker='o')
plt.title("GDP/Capita (PPP) for BRICS Countries (2000-2020)", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("GDP/Capita (PPP) ($)", fontsize=14)
plt.xticks([2000, 2010, 2020], fontsize=12)
plt.legend(title="Country", fontsize=10)
plt.tight_layout()
plt.savefig("brics_gdp_per_capita.png")
plt.show()


g7_final_data = final_brics_g7_data[final_brics_g7_data['Country'].isin(g7_countries)]

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=g7_final_data, x='Year', y='GDP/Capita (PPP)', hue='Country', marker='o')
plt.title("GDP/Capita (PPP) for G7 Countries (2000-2020)", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("GDP/Capita (PPP) ($)", fontsize=14)
plt.xticks([2000, 2010, 2020], fontsize=12)
plt.legend(title="Country", fontsize=10)
plt.tight_layout()
plt.savefig("g7_gdp_per_capita.png")
plt.show()


def calculate_gdp_growth(data):
    start_year_data = data[data['Year'] == 2000][['Country', 'GDP/Capita (PPP)']]
    end_year_data = data[data['Year'] == 2020][['Country', 'GDP/Capita (PPP)']]
    start_year_data.rename(columns={'GDP/Capita (PPP)': 'GDP_Start'}, inplace=True)
    end_year_data.rename(columns={'GDP/Capita (PPP)': 'GDP_End'}, inplace=True)
    combined_data = pd.merge(start_year_data, end_year_data, on='Country')
    combined_data['Annual Growth (%)'] = ((combined_data['GDP_End'] / combined_data['GDP_Start']) ** 
                                          (1 / 20) - 1) * 100
    return combined_data[['Country', 'Annual Growth (%)']]

brics_growth = calculate_gdp_growth(brics_data)
g7_growth = calculate_gdp_growth(g7_data)

brics_growth['Group'] = 'BRICS'
g7_growth['Group'] = 'G7'

growth_data = pd.concat([brics_growth, g7_growth])

plt.figure(figsize=(10, 6))
for group, color in zip(['BRICS', 'G7'], ['blue', 'green']):
    group_data = growth_data[growth_data['Group'] == group]
    plt.bar(group_data['Country'], group_data['Annual Growth (%)'], color=color, alpha=0.7)

plt.title('GDP/Capita Annual Growth (2000-2020)', fontsize=16)
plt.ylabel('Growth (%)', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.savefig("gdp_growth_rates.png")
plt.show()
