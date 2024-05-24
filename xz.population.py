import geopandas as gpd
import pandas as pd
# 加载数据
geo = gpd.read_file("E:\\平顶山\\geo\\geo.shp")
def map_values(value):
    if 100000 <= value <= 295474:
        return 1.0
    elif 68240 <= value <= 99999:
        return 0.9
    elif 53555 <= value <= 68239:
        return 0.8
    elif 46635 <= value <= 53554:
        return 0.7
    elif 40375 <= value <= 66634:
        return 0.6
    elif 35212 <= value <= 40374:
        return 0.5
    elif 29723 <= value <= 35211:
        return 0.4
    elif 21823 <= value <= 29722:
        return 0.3
    elif 17510 <= value <= 21822:
        return 0.2
    elif 1 <= value <= 17509:
        return 0.1
    elif value == 0:
        return 0
    else:
        return value
geo['population'] = geo['population'].map(map_values)
# 保存新数据到新的shapefile
geo.to_file("E:\\平顶山\\geo\\geo1.shp")