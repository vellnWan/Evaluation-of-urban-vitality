import geopandas as gpd
import pandas as pd
import os
gdf = gpd.read_file("E:\\平顶山\\geo\\geo.shp")
bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16.5]
labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-16.5']
gdf['grade_range'] = pd.cut(gdf['grade'], bins=bins, labels=labels, right=False)
path = "E:\\平顶山\\geo\\区县"
files = [f"{path}\\{f}" for f in os.listdir(path) if f.endswith(".shp")]
result = []
for file in files:
    admin_gdf = gpd.read_file(file)
    gdf_clip = gpd.overlay(gdf, admin_gdf, how='intersection')
    county_name = os.path.split(file)[-1].split(".")[0]
    count = gdf_clip['grade_range'].value_counts().sort_index().to_dict()
    temp_df = pd.DataFrame({'County': county_name,' Range': count.index,'Count': count.values})
    result_df = pd.concat([result_df, temp_df])
pivot_df = result_df.pivot(index='Range', columns='County', values='Count')
pivot_df.fillna(0, inplace = True)


