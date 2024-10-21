from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

accuracys = 0.0
for i in range(20):
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 数据标准化
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 创建高斯朴素贝叶斯分类器
    gnb_classifier = GaussianNB()

    # 在训练集上训练模型
    gnb_classifier.fit(X_train_scaled, y_train)

    # 在测试集上进行预测
    y_pred = gnb_classifier.predict(X_test_scaled)

    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    accuracys += accuracy
print("正确率为：", accuracys/20)
