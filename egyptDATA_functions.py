import geopandas as gpd
import matplotlib as plt
aswan_gdf = gpd.read_file('https://github.com/CSF-AIC-Internship/AIC_CSFINT_REPO/blob/27a565af054b7770566c016080c503a35b10dd42/Export_Locate_the_Shi__Qarya_2017_polygon.shp')
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