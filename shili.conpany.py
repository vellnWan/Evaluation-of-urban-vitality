import geopandas as gpd
# 加载网格数据
df_geo = gpd.read_file('E:\\平顶山\\geo\\geo.shp')
# 加载POI数据
df_poi = gpd.read_file('E:\\平顶山\\poi\\poi.shp')
# 从POI数据中筛选出type1 字段值为 "公司企业" 的POI
df_company = df_poi[df_poi['type1'] =='公司企业']
#执行空间连接操作
sjoined = gpd.sjoin(df_geo, df_company, predicate='intersects')
#在空间连接操作之后，直接计算每个网格中的公司企业数目
counts = sjoined.groupby(sjoined.index)['type1'].count()
# 使用reindex以确保所有的行都有值
counts = counts.reindex(df_geo.index, fill_value=0)
# 将每个网格中的公司企业数量添加到原始 geo DataFrame 中的 'company' 列
df_geo['company'] = counts
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
df_geo['company'] = df_geo['company'].map(map_values)
# 保存 DataFrame 到新的 shp 文件
df_geo.to_file('E:\\平顶山\\geo\\geo_updated.shp')