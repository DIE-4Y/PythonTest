from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

# 加载数据集
iris = load_iris()
X = iris.data[:, :2]  # 选择花萼进行分类
y = iris.target

# 数据预处理：标准化特征值
scaler = StandardScaler()
X = scaler.fit_transform(X)

accuracys = 0.0
for i in range(20):
    # 划分数据集为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 创建SVM分类器并训练模型
    svm_classifier = SVC(kernel='linear', C=1.0, random_state=42)
    svm_classifier.fit(X_train, y_train)

    # 使用训练好的模型进行预测
    y_pred = svm_classifier.predict(X_test)

    # 计算模型准确率
    accuracy = accuracy_score(y_test, y_pred)
    accuracys += accuracy
print("正确率为：",accuracys/20)

"""
# 可视化分类结果
# 创建网格以绘制决策边界
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# 绘制决策边界
Z = svm_classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

# 绘制训练数据点
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.coolwarm, edgecolors='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('SVM Classification Results')
plt.show()
"""