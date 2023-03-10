import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

'''
Program to plot a world map choropleth showing the annual change
in total energy consumption for each country in the world map
'''

df = pd.read_csv(r'C:\Users\veera\Downloads\abs-change-energy-consumption.csv')
print(df.columns)

energy_df_copy = df.loc[df['Year'] == 2021]
energy_df_copy = energy_df_copy.copy()
energy_df_copy.rename({"Code":"ISO_A3"}, axis=1, inplace=True)
#print(energy_df_copy.columns)

shapes = gpd.read_file(r'C:\Users\veera\Downloads\world_shape_files.shp')
country_shapes = shapes[["ISO_A3","geometry"]]
# Merge the country shapes and the annual change
r_energy = energy_df_copy.merge(country_shapes, on='ISO_A3')

# Now to plot the stuff as a geopandas
renewables_gdf = gpd.GeoDataFrame(r_energy, geometry=r_energy["geometry"])
sum1 = r_energy['Annual change in primary energy consumption (TWh)'].sum()
avg = sum1/len(r_energy)
print(avg)
vmin = -100
#vmax = r_energy['Annual change in primary energy consumption (TWh)'].max()
vmax = 800
vcenter = 0
norm = TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)

fig, ax = plt.subplots(1, figsize=(15, 6))
ax.axis('off')
ax.set_title('Annual change in primary energy consumption (TWh)', fontdict={'fontsize': '15', 'fontweight' : '3'})
renewables_gdf.plot(column='Annual change in primary energy consumption (TWh)', cmap="RdBu", norm = norm, ax=ax, legend=True,
                    legend_kwds={'label': "Annual change in primary energy consumption (TWh)",'orientation': "horizontal"},
                    missing_kwds = {'color':'lightgrey',  "hatch": "///",  "label": "Missing values","edgecolor": "red"})
plt.show()





