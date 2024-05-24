import geopandas as gpd
# 读取 '缓冲区合并.shp' 和 'geo.shp' 文件
gdf_merged = gpd.read_file(r'E:\平顶山\水系\water缓冲区.shp').to_crs(epsg=32650)
gdf_geo = gpd.read_file(r'E:\\平顶山\\geo\\geo.shp').to_crs(epsg=32650)
# 使用 sjoin() 找出每个网格中缓冲区的部分
sjoined = gpd.sjoin(gdf_geo, gdf_merged, how='left', predicate='intersects')
# 在每个网格中，计算与缓冲区相交的部分的面积
sjoined['water'] = sjoined.apply(lambda row: row.geometry.buffer(0).intersection(gdf_merged.unary_union).area, axis=1)
# 删除无用的列
sjoined.drop(columns=['index_right'], inplace=True)
# 保存处理后的文件
sjoined.to_file(r"E:\\平顶山\\geo\\geo_updated.shp")