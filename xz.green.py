import geopandas as gpd
import pandas as pd
# 加载数据
geo = gpd.read_file("E:\\平顶山\\geo\\geo.shp")
def map_values(value):
    if 3200 <= value <= 6911:
        return 1.0
    elif 6912 <= value <= 7951:
        return 0.9
    elif 7952 <= value <= 8487:
        return 0.8
    elif 8488 <= value <= 8896:
        return 0.7
    elif 8897 <= value <= 9243:
        return 0.6
    elif 9244 <= value <= 9490:
        return 0.5
    elif 9491 <= value <= 9692:
        return 0.4
    elif 9693 <= value <= 9871:
        return 0.3
    elif 9872 <= value <= 9999:
        return 0.2
    elif value == 10000:
        return 0.1
    elif value == 32767:
        return 0
    else:
        return value
geo['green'] = geo['green'].map(map_values)
# 保存新数据到新的shapefile
geo.to_file("E:\\平顶山\\geo\\geo1.shp")