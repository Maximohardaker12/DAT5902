# DAT5902 Final Project: Professional Software and Career Practices

## Overview
This repository contains the code and resources for the final project of the DAT5902 module. The project focuses on analysing a high-quality dataset to test a hypothesis, perform data analysis, and visualize trends. The main goal is to provide insights into global GDP per capita trends, comparing developed (G7) and developing (BRICS) economies.

## Objectives
1. **Hypothesis**: Developed countries (G7) have a higher GDP per capita (PPP) compared to developing countries (BRICS), but BRICS countries demonstrate higher GDP per capita growth rates in the 21st century.
2. **Analysis Goals**:
   - Compare GDP per capita (PPP) trends for G7 and BRICS nations.
   - Examine annualized GDP per capita growth rates (2000–2020).

## Repository Contents
- **`data/`**: Contains the dataset used for analysis.
  - `gdp_per_capita.csv`: Source data obtained from [Our World in Data](https://ourworldindata.org/grapher/gdp-per-capita-worldbank).
- **`code/`**: Python scripts for data processing and analysis.
  - `main_analysis.py`: Core script to clean, process, and visualize data.
  - `unit_tests.py`: Unit tests to verify analysis outputs.
- **`tests/`**: Folder containing unit tests and integration tests.
- **`README.md`**: Documentation for this repository.
- **Graphs and Outputs**:
  - `brics_gdp_per_capita.png`: Trends in GDP per capita for BRICS nations.
  - `g7_gdp_per_capita.png`: Trends in GDP per capita for G7 nations.
  - `gdp_growth_rates.png`: Comparison of GDP growth rates for BRICS and G7 countries.

## Key Results
1. **GDP per Capita (PPP)**:
   - G7 countries maintain significantly higher GDP per capita (PPP) compared to BRICS countries.
   - BRICS countries show faster growth over the 20-year period (2000–2020).

2. **Growth Rates**:
   - China leads BRICS nations with the highest growth rate.
   - G7 countries exhibit slower, more stable growth patterns.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Maximohardaker12/DAT5902.git
   cd DAT5902
