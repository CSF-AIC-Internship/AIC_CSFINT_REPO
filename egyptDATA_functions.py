pip install geopandas
import geopandas as gpd
import matplotlib as plt
from google.colab import drive
drive.mount('/content/drive')
aswan_gdf = gpd.read_file('/content/drive/MyDrive/Colab Notebooks/EgyptData/aswan_Shi__Qarya_2017/Export_Locate_the_Shi__Qarya_2017_polygon.shp')
aswan_gdf.head()
aswan_gdf.shape
aswan_gdf['centroid'] = aswan_gdf['geometry'].centroid
aswan_gdf.shape
aswan_gdf.head()
aswan_gdf.columns
df_bounds = aswan_gdf.bounds
df_bounds
aswan_gdf['combined'] = df_bounds[df_bounds.columns].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
aswan_gdf