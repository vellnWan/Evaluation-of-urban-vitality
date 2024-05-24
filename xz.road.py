import geopandas as gpd
import pandas as pd
# 加载数据
geo = gpd.read_file("E:\\平顶山\\geo\\geo.shp")
def map_values(value):
    if 4479.24 <= value <= 16592:
        return 1.0
    elif 3473.56 <= value <= 4479.23:
        return 0.9
    elif 2904.51 <= value <= 3473.55:
        return 0.8
    elif 2425.32 <= value <= 2904.50:
        return 0.7
    elif 2042.34 <= value <= 2425.31:
        return 0.6
    elif 1606.65 <= value <= 2042.33:
        return 0.5
    elif 1208.97 <= value <= 1606.64:
        return 0.4
    elif 678.08 <= value <= 1208.96:
        return 0.3
    elif 63.55 <= value <= 678.07:
        return 0.2
    elif 0.01 <= value <= 63.54:
        return 0.1
    elif value == 0:
        return 0
    else:
        return value
geo['road'] = geo['road'].map(map_values)
# 保存新数据到新的shapefile
geo.to_file("E:\\平顶山\\geo\\geo1.shp")