
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# 导入数据集iris
iris = load_iris()
data = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

# 计算属性
max_values = data.max()
min_values = data.min()
mean_values = data.mean()
std_values = data.std()

# 对属性特征可视化
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot for maximum values
sns.barplot(x=max_values.index, y=max_values.values, ax=axs[0, 0])
axs[0, 0].set_title('Maximum Values')

# Plot for minimum values
sns.barplot(x=min_values.index, y=min_values.values, ax=axs[0, 1])
axs[0, 1].set_title('Minimum Values')

# Plot for mean values
sns.barplot(x=mean_values.index, y=mean_values.values, ax=axs[1, 0])
axs[1, 0].set_title('Mean Values')

# Plot for standard deviation values
sns.barplot(x=std_values.index, y=std_values.values, ax=axs[1, 1])
axs[1, 1].set_title('Standard Deviation Values')

plt.tight_layout()
plt.show()

# 绘制箱线图
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
for i, feature in enumerate(iris['feature_names']):
    sns.boxplot(x=data['target'], y=data[feature], ax=axs[i // 2, i % 2])
    axs[i // 2, i % 2].set_title(f'{feature} Boxplot by Target Class')
plt.tight_layout()
plt.show()

# 绘制散点图
fig, axs = plt.subplots(2, 2, figsize=(12, 6))

# 花瓣长度 vs 花瓣宽度
sns.scatterplot(x='petal width (cm)', y='petal length (cm)', hue='target', data=data, ax=axs[0, 0])
axs[0, 0].set_title('Petal Width vs Petal Length')

# 花萼长度 vs 花萼宽度
sns.scatterplot(x='sepal width (cm)', y='sepal length (cm)', hue='target', data=data, ax=axs[0, 1])
axs[0, 1].set_title('Sepal Width vs Sepal Length')

# 花瓣长度 vs 花萼宽度
sns.scatterplot(x='petal width (cm)', y='sepal length (cm)', hue='target', data=data, ax=axs[1, 0])
axs[1, 0].set_title('Petal Width vs Sepal Length')

# 花瓣长度 vs 花萼宽度
sns.scatterplot(x='petal width (cm)', y='sepal length (cm)', hue='target', data=data, ax=axs[1, 1])
axs[1, 1].set_title('Petal Width vs Sepal Length')

plt.tight_layout()
plt.show()



# 导入数据集iris
iris = load_iris()
data = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

# 不同的训练集比例
test_sizes = [0.1, 0.2, 0.3, 0.4, 0.5]

# 存储不同比例下的准确率
accuracies = []

# 对每个训练集比例进行循环划分
for test_size in test_sizes:
    # 存储每个比例下的准确率
    accuracy_per_size = []
    for i in range(20):
        # 划分数据集为训练集和测试集
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

        # 定义并训练决策树模型
        dt_classifier = DecisionTreeClassifier(criterion='gini')
        dt_classifier.fit(X_train, y_train)

        # 预测并计算准确率
        y_pred = dt_classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_per_size.append(accuracy)

    # 计算当前比例下的平均准确率并存储
    average_accuracy = sum(accuracy_per_size) / len(accuracy_per_size)
    accuracies.append(average_accuracy)

# 输出不同比例下的平均准确率
for i, test_size in enumerate(test_sizes):
    print("训练集比例为 {}: 平均准确率为 {}".format(test_size, accuracies[i]))

# 可视化决策树
"""plt.figure(figsize=(20, 10))
plot_tree(dt_classifier, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()
"""
