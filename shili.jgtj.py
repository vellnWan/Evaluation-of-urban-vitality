import geopandas as gpd
import pandas as pd
import os
# 读取shp文件
gdf = gpd.read_file("E:\\平顶山\\geo\\geo.shp")
# 设定grade字段的区间以及对应的标签
bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16.5]
labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-16.5']
# 对grade字段进行离散化
gdf['grade_range'] = pd.cut(gdf['grade'], bins=bins, labels=labels, right=False)
# 生成空的DataFrame以接收结果
result_df = pd.DataFrame(columns=['County', 'Range', 'Count'])
# 遍历每一个行政区划shp
path = "E:\\平顶山\\geo\\区县"
files = [f"{path}\\{f}" for f in os.listdir(path) if f.endswith(".shp")]
for file in files:
    admin_gdf = gpd.read_file(file)
    gdf_clip = gpd.overlay(gdf, admin_gdf, how='intersection')
    county_name = os.path.split(file)[-1].split(".")[0]  # 获取县名（文件名）
    count = gdf_clip['grade_range'].value_counts().sort_index()  # 统计每个区间的数量
    temp_df = pd.DataFrame({'County': county_name, 'Range': count.index, 'Count': count.values})  # 转化为DataFrame
    result_df = pd.concat([result_df, temp_df])  # 添加到结果DataFrame中
# 使用pivot将df转换为你需要的形式
pivot_df = result_df.pivot(index='Range', columns='County', values='Count')
# 填充NaN值为0
pivot_df.fillna(0, inplace=True)
# 保存为Excel文件
pivot_df.to_excel("E:\\平顶山\\城市活力统计结果.xlsx")