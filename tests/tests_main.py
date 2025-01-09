import unittest
import pandas as pd
from main import calculate_gdp_growth

class TestGDPAnalysis(unittest.TestCase):

    def setUp(self):
        self.data = pd.read_csv("data/gdp_per_capita.csv")
        self.data.rename(columns={'Entity': 'Country', 
                                  'GDP per capita, PPP (constant 2017 international $)': 'GDP/Capita (PPP)'}, inplace=True)
        self.brics_countries = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
        self.g7_countries = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']

if __name__ == "__main__":
    unittest.main()
