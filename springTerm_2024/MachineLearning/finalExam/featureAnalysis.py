import pandas as pd
import matplotlib.pyplot as plt
import sns
import seaborn as sb

# 读取CSV文件
df = pd.read_csv('stuInform.csv')

# 按性别拆分数据
male_data = df[df['gender'] == '男']
female_data = df[df['gender'] == '女']

# 身高与体重
plt.scatter(male_data['height(cm)'], male_data['weight(kg)'], c='blue', label='male')
plt.scatter(female_data['height(cm)'], female_data['weight(kg)'], c='red', label='female')
plt.title('height and weight')
plt.xlabel('height(cm)')
plt.ylabel('weight')
# 添加图例
plt.legend()
# 显示图表
plt.show()



# 身高与年龄
plt.scatter(male_data['height(cm)'], male_data['age'], c='blue', label='male')
plt.scatter(female_data['height(cm)'], female_data['age'], c='red', label='female')
plt.title('height and age')
plt.xlabel('height(cm)')
plt.ylabel('age')
# 添加图例
plt.legend()
# 显示图表
plt.show()

# 年龄与体重
plt.scatter(male_data['weight(kg)'], male_data['age'], c='blue', label='male')
plt.scatter(female_data['weight(kg)'], female_data['age'], c='red', label='female')
plt.title('age and weight')
plt.xlabel('age')
plt.ylabel('weight')
# 添加图例
plt.legend()
# 显示图表
plt.show()

# 计算属性之间的相关性
correlation_matrix = df[['age', 'height(cm)', 'weight(kg)']].corr()

# 创建热力图
sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)

# 显示热力图
plt.show()
