import pandas as pd
# 读取txt文件并转为DataFrame
df = pd.read_csv("E:\\平顶山\\城市活力统计结果.txt", header=None, sep=":",encoding='GBK')
# 设定列名
df.columns = ['County', 'Range', 'Count']
# 使用pivot将df转换为你需要的形式
pivot_df = df.pivot(index='Range', columns='County', values='Count')
# 填充NaN值为0
pivot_df.fillna(0, inplace=True)
# 保存为Excel文件
pivot_df.to_excel("E:\\平顶山\\城市活力统计结果.xlsx")