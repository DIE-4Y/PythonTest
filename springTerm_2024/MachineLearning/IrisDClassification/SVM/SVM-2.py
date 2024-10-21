from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt

# 加载数据集
iris = load_iris()
X = iris.data[:, 2:4]  # 选择花瓣进行分类
y = iris.target


accuracys = 0.0
for i in range(20):
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 数据标准化
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 创建SVM分类器
    svm_classifier = SVC(kernel='linear', C=1.0, random_state=42)

    # 在训练集上训练模型
    svm_classifier.fit(X_train_scaled, y_train)

    # 在测试集上评估模型
    accuracy = svm_classifier.score(X_test_scaled, y_test)
    accuracys += accuracy
print("分类正确率为：", accuracys/20)

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
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.title('SVM Classification Results')
plt.show()

"""