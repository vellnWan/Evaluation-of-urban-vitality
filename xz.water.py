import geopandas as gpd
import pandas as pd
# Load the shapefile
gdf = gpd.read_file('E:\\平顶山\\geo\\geo.shp')
# Define the mapping function
def map_values(value):
    if 1 <= value < 809.418355617:
        return 0.1
    elif 809.418355618 <= value < 56095.258635926:
        return 0.2
    elif 56095.258635927 <= value < 187557.375650405:
        return 0.3
    elif 187557.375650406 <= value < 372131.417333291:
        return 0.4
    elif 372131.417333292 <= value < 599480.536607465:
        return 0.5
    elif 599480.536607466 <= value < 791931.816790531:
        return 0.6
    elif 791931.816790532 <= value < 1000168.927528608:
        return 0.7
    elif 1000168.927528609 <= value < 1161996.734360962:
        return 0.8
    elif 1161996.734360963 <= value < 1191778.102168682:
        return 0.9
    elif 1191778.102168683 <= value <= 1191778.102168749:
        return 1.0
    elif value == 0:
        return 0
    else:
        return value
# Apply the function to the 'water' column
gdf['water'] = gdf['water'].map(map_values)
# Save the modified GeoDataFrame
gdf.to_file('E:\\平顶山\\geo\\geo1.shp')