from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
import numpy as np

# 载入数据集
iris_dataset = load_iris()
X = iris_dataset['data']
Y = iris_dataset['target']

# n的范围和正确率列表
n_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
accuracy_list = []

for i in n_list:
    accuracy = 0
    for j in range(20):
        # 数据划分
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        # 训练阶段
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, Y_train)#构建基于训练集的模型
        #测试评估模型
        Y_pred=knn.predict(X_test)
        accuracy += accuracy_score(Y_test, Y_pred)
    print("Test range = {} accuracy is :{:.6f}".format(i, accuracy/20))
    accuracy_list.append(accuracy / 20)

# 绘制结果折线图
plt.bar(n_list, accuracy_list)
plt.title("different k range with accuracys")
plt.xlabel("K range")
plt.ylabel("Accuracy")
plt.show()
