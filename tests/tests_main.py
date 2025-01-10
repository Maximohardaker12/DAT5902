import unittest
import pandas as pd

<<<<<<< HEAD
=======

>>>>>>> c6fa700015b93f751c589b9cff673a6e39dd9f11
from main.main import calculate_gdp_growth  

class TestGDPAnalysis(unittest.TestCase):

    def setUp(self):
        
        self.data = pd.read_csv("data/gdp_per_capita.csv")
        self.data.rename(columns={'Entity': 'Country', 
                                  'GDP per capita, PPP (constant 2017 international $)': 'GDP/Capita (PPP)'}, inplace=True)
        self.brics_countries = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
        self.g7_countries = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']

    def test_data_loading(self):
        """Test if the data is loaded correctly and essential columns are present."""
        self.assertFalse(self.data.empty, "Dataset should not be empty.")
        self.assertIn('Country', self.data.columns, "Column 'Country' should be present.")
        self.assertIn('GDP/Capita (PPP)', self.data.columns, "Column 'GDP/Capita (PPP)' should be present.")

    def test_filtering_brics_data(self):
        """Test if BRICS data is filtered correctly."""
        brics_data = self.data[self.data['Country'].isin(self.brics_countries)]
        self.assertEqual(set(brics_data['Country']), set(self.brics_countries), "Filtered BRICS data should match expected countries.")

    def test_filtering_g7_data(self):
        """Test if G7 data is filtered correctly."""
        g7_data = self.data[self.data['Country'].isin(self.g7_countries)]
        self.assertEqual(set(g7_data['Country']), set(self.g7_countries), "Filtered G7 data should match expected countries.")

    def test_calculate_gdp_growth(self):
        """Test if GDP growth calculation is correct."""
        brics_data = self.data[self.data['Country'].isin(self.brics_countries)]
        growth_data = calculate_gdp_growth(brics_data)
        self.assertIn('Annual Growth (%)', growth_data.columns, "Growth calculation should include 'Annual Growth (%)' column.")
        self.assertGreater(growth_data['Annual Growth (%)'].mean(), 0, "Average growth rate should be greater than zero.")

    def test_brics_visualisation(self):
        """Test if visualisation data for BRICS contains all expected countries."""
        brics_data = self.data[self.data['Country'].isin(self.brics_countries)]
        filtered_data = brics_data[(brics_data['Year'] >= 2000) & (brics_data['Year'] <= 2020)]
        self.assertEqual(set(filtered_data['Country']), set(self.brics_countries), "BRICS visualisation data should include all BRICS countries.")

if __name__ == "__main__":
    unittest.main()
