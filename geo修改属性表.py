import geopandas as gpd
import numpy as np
# Load the existing shapefile
gdf = gpd.read_file('E:\\平顶山\\绿地\\绿地.shp')
# Adding new fields
fields = ['water', 'company', 'finance', 'shop', 'food', 
          'lodging', 'live', 'culture', 'scape', 'sport', 
          'population', 'traffic', 'public', 'medical', 
          'government', 'road']
for field in fields:
    gdf[field] = np.nan
# Save the updated GeoDataFrame as a new shapefile
gdf.to_file('E:\\平顶山\\geo\\geo.shp')
print("File with additional fields has been written to 'E:\\平顶山\\geo\\geo.shp'")