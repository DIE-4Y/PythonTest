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


# 准备数据
X = iris.data
y = iris.target

"""
# 不同的训练集比例
test_sizes = [0.1, 0.2, 0.3, 0.4, 0.5]

# 存储不同比例下的准确率
accuracies = []

# 对每个训练集比例进行循环划分
for test_size in test_sizes:
    # 存储每个比例下的准确率
    accuracy_per_size = []
"""
accuracy = 0.0
for i in range(20):
    # 划分数据集为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 定义并训练决策树模型
    dt_classifier = DecisionTreeClassifier(criterion='gini')
    dt_classifier.fit(X_train, y_train)

    # 预测并计算准确率
    y_pred = dt_classifier.predict(X_test)
    accuracy += accuracy_score(y_test, y_pred)
print("准确率为：", accuracy / 20)

# 可视化决策树
plt.figure(figsize=(20, 10))
plot_tree(dt_classifier, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()

