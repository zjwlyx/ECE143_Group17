import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

'''
Program to plot 2 bar graphs showing the growth in renewable energy 
and total energy consumption over the past 20 years
'''
raw = pd.read_csv("C:/Users/veera/Downloads/archive/World Energy Consumption.csv")
print(raw.columns)
# Total Renewable Energy Consumption
energy_consumption = ["coal_consumption", "gas_consumption","iso_code","country", "year", "renewables_consumption","other_renewable_consumption","hydro_consumption","solar_consumption","wind_consumption", "fossil_fuel_consumption"]
renewable_consumption2 = ["fossil_fuel_consumption","hydro_consumption","wind_consumption","solar_consumption","other_renewable_consumption"]
renewable_consumption1 = ["hydro_consumption","wind_consumption","solar_consumption","other_renewable_consumption"]
energy_df = raw[energy_consumption]

# Create dataframe for yearly energy consumption
year_range = energy_df["year"].isin(range(2000,2020))
energy_df = energy_df[year_range]

# Create a copy of the energy_df dataframe to avoid the warning
energy_df_copy = energy_df.copy()
energy_df_copy.rename({"iso_code":"ISO_A3"}, axis=1, inplace=True)

bar1 = energy_df_copy.groupby('year')[renewable_consumption1].sum()
bar1.reset_index(level=0, inplace=True)

colors2 = ['lightgrey', 'steelblue', 'lightskyblue', 'peru', 'khaki']
colors1 = ['steelblue', 'lightskyblue', 'peru', 'khaki']

# Plot the stacked bar graph for Global renewable energy consumption
bar1.plot(x='year', ylabel='Terrawatt Hours of Energy', kind='bar', stacked=True, figsize=(20,8), title='Global Renewable Energy Consumption between 2000-2019', color = colors1)
plt.show()

bar2 = energy_df_copy.groupby('year')[renewable_consumption2].sum()
bar2.reset_index(level=0, inplace=True)

# Plot the stacked bar graph for Global renewable + Fossil fuel energy consumption
bar2.plot(x='year', ylabel='Terrawatt Hours of Energy', kind='bar', stacked=True, figsize=(20,8), title='Global Renewable + fossil fuel Energy Consumption between 2000-2019', color = colors2)
plt.show()
