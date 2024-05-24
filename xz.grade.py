import geopandas as gpd
gdf = gpd.read_file("E:\\平顶山\\geo\\geo.shp")
cols_to_add = ['green', 'water', 'company', 'finance', 'shop', 'food',
          'lodging', 'live', 'culture', 'scape', 'sport',
          'population', 'traffic', 'public', 'medical', 'road',
          'goverment']
gdf['grade'] = gdf[cols_to_add].sum(axis = 1)
gdf.to_file("E:\\平顶山\\geo\\geo1.shp")


