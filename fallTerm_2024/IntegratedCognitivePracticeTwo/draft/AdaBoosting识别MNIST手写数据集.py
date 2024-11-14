import numpy as np
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 加载MNIST数据集
data_path = './data'
mnist = datasets.MNIST(root=data_path, train=True, download=False, transform=transforms.ToTensor())

# 将数据转换为numpy数组
X = mnist.data.numpy().reshape(-1, 28 * 28)
y = mnist.targets.numpy()

# 划分训练集与测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 实例化AdaBoost分类器
n_estimators = 50
ada_classifier = AdaBoostClassifier(n_estimators=n_estimators, random_state=42)

# 训练并记录训练和测试的准确性
train_accuracies = []
test_accuracies = []

for i in range(1, n_estimators + 1):
    ada_classifier.n_estimators = i
    ada_classifier.fit(X_train, y_train)

    # 计算训练和测试准确性
    train_accuracy = ada_classifier.score(X_train, y_train)
    test_accuracy = ada_classifier.score(X_test, y_test)

    train_accuracies.append(train_accuracy)
    test_accuracies.append(test_accuracy)

# 预测
y_pred = ada_classifier.predict(X_test)

# 评估模型
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 可视化准确性变化
plt.figure(figsize=(10, 6))
plt.plot(range(1, n_estimators + 1), train_accuracies, label='Train Accuracy', marker='o')
plt.plot(range(1, n_estimators + 1), test_accuracies, label='Test Accuracy', marker='o')
plt.title('Train and Test Accuracy vs. Number of Estimators')
plt.xlabel('Number of Estimators')
plt.ylabel('Accuracy')
plt.xticks(range(1, n_estimators + 1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.legend()
plt.grid()
plt.show()

# 可视化一些测试样本的预测结果
def plot_digits(data, labels, predictions, n=10):
    plt.figure(figsize=(15, 5))
    for index in range(n):
        plt.subplot(2, n, index + 1)
        plt.imshow(data[index].reshape(28, 28), cmap='gray')
        plt.title(f"True: {labels[index]}\nPred: {predictions[index]}")
        plt.axis('off')
    plt.show()


# 展示10个样本的结果
plot_digits(X_test, y_test, y_pred, n=10)
