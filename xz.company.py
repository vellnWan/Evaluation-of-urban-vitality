import geopandas as gpd
import pandas as pd
# 加载数据
geo = gpd.read_file("E:\\平顶山\\geo\\geo.shp")
def map_values(value):
    if 101 <= value <= 370:
        return 1.0
    elif 31 <= value <= 100:
        return 0.9
    elif 14 <= value <= 30:
        return 0.8
    elif 9 <= value <= 13:
        return 0.7
    elif 7 <= value <= 8:
        return 0.6
    elif 5 <= value <= 6:
        return 0.5
    elif value == 4:
        return 0.4
    elif value == 3:
        return 0.3
    elif value == 2:
        return 0.2
    elif value == 1:
        return 0.1
    elif value == 0:
        return 0
    else:
        return value
geo['company'] = geo['company'].map(map_values)
# 保存新数据到新的shapefile
geo.to_file("E:\\平顶山\\geo\\geo1.shp")