import pandas as pd

# 读取Excel文件
df = pd.read_excel('2024机器学习期末考试_22智能班.xlsx')

# 删除序号列（假设序号列的名称是'序号'）
df = df.drop(columns=['序号'])

# 保存为CSV文件
df.to_csv('stuInform.csv', index=False)
