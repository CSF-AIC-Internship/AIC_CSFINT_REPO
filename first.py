import plotly.express as px

# create a map of area, where houses from data set located
fig = px.scatter_mapbox(data, #our data set
                        lat="lat", lon="long", #location
                        color="price", #select a column for ranking
                        hover_name="price",
                        hover_data=["bedrooms", "bathrooms"],
                        color_discrete_sequence=["green"],
                        size_max=15,
                        zoom=8,
                        width=900, height=600, #map size
                        title =  'Map of area, check location')
#style of map
fig.update_layout(mapbox_style="open-street-map")
fig.show(config={'scrollZoom': False})