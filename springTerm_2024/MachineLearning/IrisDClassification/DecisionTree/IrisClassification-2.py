import math
from typing import Union
import collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class DecisionNode(object):
    def __init__(self, f_idx, threshold, value=None, L=None, R=None):
        self.f_idx = f_idx  # 属性的下标，表示通过下标为f_idx的属性来划分样本
        self.threshold = threshold  # 下标 `f_idx` 对应属性的阈值
        self.value = value  # 如果该节点是叶子节点，对应的是被划分到这个节点的数据的类别
        self.L = L  # 左子树
        self.R = R  # 右子树

def find_best_threshold(dataset: np.ndarray, f_idx: int):
    best_gini = math.inf
    best_threshold = None
    dataset_sorted = sorted(list(set(dataset[:, f_idx].reshape(-1))))
    candidate = []
    for i in range(len(dataset_sorted) - 1):
        candidate.append(round((dataset_sorted[i] + dataset_sorted[i + 1]) / 2.0, 2))

    for threshold in candidate:
        L, R = split_dataset(dataset, f_idx, threshold)
        gini = calculate_gini_index(dataset, L, R)
        if gini < best_gini:
            best_gini = gini
            best_threshold = threshold

    return best_threshold, best_gini

def calculate_gini(dataset: np.ndarray):
    scale = dataset.shape[0]  # 多少条数据
    d = {}
    for data in dataset:
        key = data[-1]
        if key in d:
            d[key] += 1
        else:
            d[key] = 1

    gini = 1.0
    for key in d.keys():
        p = d[key] / scale
        gini -= p * p
    return gini

def calculate_gini_index(dataset, l, r):
    gini_index = len(l) / len(dataset) * calculate_gini(l) + len(r) / len(dataset) * calculate_gini(r)
    return gini_index

def split_dataset(X: np.ndarray, f_idx: int, threshold: float):
    L = X[:, f_idx] < threshold
    R = ~L
    return X[L], X[R]

def majority_count(dataset):
    class_list = [data[-1] for data in dataset]
    return collections.Counter(class_list).most_common(1)[0][0]

 # 寻找分类节点
def build_tree(dataset: np.ndarray, f_idx_list: list, split_choice: str):
    class_list = [data[-1] for data in dataset]  # 类别
    # 全属于同一类别
    if class_list.count(class_list[0]) == len(class_list):
        return DecisionNode(None, None, value=class_list[0])
    # 若属性都用完, 标记为类别最多的那一类
    elif len(f_idx_list) == 0:
        value = collections.Counter(class_list).most_common(1)[0][0]
        return DecisionNode(None, None, value=value)
    else:
        # 找到划分 增益最大的属性 4个属性
        best_gain = -math.inf
        best_gini = math.inf
        best_threshold = None
        best_f_idx = None
        for i in f_idx_list:
            threshold, gain = find_best_threshold(dataset, i)
            if gain < best_gini:
                best_gini = gain
                best_threshold = threshold
                best_f_idx = i
        son_f_idx_list = f_idx_list.copy()
        son_f_idx_list.remove(best_f_idx)
        # 创建分支
        L, R = split_dataset(dataset, best_f_idx, best_threshold)
        if len(L) == 0:
            L_tree = DecisionNode(None, None, majority_count(dataset))  # 叶子节点
        else:
            L_tree = build_tree(L, son_f_idx_list, split_choice)  # return DecisionNode
        if len(R) == 0:
            R_tree = DecisionNode(None, None, majority_count(dataset))  # 叶子节点
        else:
            R_tree = build_tree(R, son_f_idx_list, split_choice)  # return DecisionNode
        return DecisionNode(best_f_idx, best_threshold, value=None, L=L_tree, R=R_tree)

def predict_one(model: DecisionNode, data):
    if model.value is not None:
        return model.value
    else:
        feature_one = data[model.f_idx]
        branch = None
        if feature_one >= model.threshold:
            branch = model.R  # 走右边
        else:
            branch = model.L  # 走左边
        return predict_one(branch, data)

def predict_accuracy(y_predict, y_test):
    y_predict = y_predict.tolist()
    y_test = y_test.tolist()
    count = 0
    # count = np.sum(y_predict == y_test)
    for i in range(len(y_predict)):
        if int(y_predict[i]) == y_test[i]:
            count = count + 1
    accuracy = count / len(y_predict)
    return accuracy

class SimpleDecisionTree(object):
    def __init__(self, split_choice, min_samples: int = 1, min_gain: float = 0, max_depth: Union[int, None] = None,
                 max_leaves: Union[int, None] = None):
        self.split_choice = split_choice

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        dataset_in = np.c_[X, y]
        f_idx_list = [i for i in range(X.shape[1])]
        self.my_tree = build_tree(dataset_in, f_idx_list, self.split_choice)

    def predict(self, X: np.ndarray) -> np.ndarray:
        predict_list = []
        for data in X:
            predict_list.append(predict_one(self.my_tree, data))
        return np.array(predict_list)

if __name__ == "__main__":

    predict_accuracy_all = []

    # 导入数据集iris
    iris = load_iris()
    data = pd.DataFrame(data=np.c_[iris['data'], iris['target']],columns=iris['feature_names'] + ['target'])

    # 特征分析
    analysis = data.describe(percentiles=[0.25, 0.5, 0.75]).transpose()

    # 设置 seaborn 样式
    sns.set(style="whitegrid")

    # 绘制直方图并添加统计量标签
    plt.figure(figsize=(12, 6))
    for i, feature in enumerate(iris['feature_names']):
        sns.histplot(data[feature], kde=True)
        plt.title(f'{feature} Distribution')
        plt.axvline(analysis.loc[feature, 'mean'], color='r', linestyle='--',
                    label=f'Mean: {analysis.loc[feature, "mean"]:.2f}')
        plt.axvline(analysis.loc[feature, 'std'], color='g', linestyle='--',
                    label=f'Std: {analysis.loc[feature, "std"]:.2f}')
        plt.axvline(analysis.loc[feature, 'max'], color='b', linestyle='--',
                    label=f'Max: {analysis.loc[feature, "max"]:.2f}')
        plt.axvline(analysis.loc[feature, 'min'], color='y', linestyle='--',
                    label=f'Min: {analysis.loc[feature, "min"]:.2f}')
        plt.axvline(analysis.loc[feature, '25%'], color='m', linestyle='--',
                    label=f'Q1: {analysis.loc[feature, "25%"]:.2f}')
        plt.axvline(analysis.loc[feature, '50%'], color='c', linestyle='--',
                    label=f'Q2: {analysis.loc[feature, "50%"]:.2f}')
        plt.axvline(analysis.loc[feature, '75%'], color='k', linestyle='--',
                    label=f'Q3: {analysis.loc[feature, "75%"]:.2f}')
        plt.legend()
        plt.show()

    # 绘制箱线图
    plt.figure(figsize=(12, 6))
    for i, feature in enumerate(iris['feature_names']):
        sns.boxplot(x='target', y=feature, data=data)
        plt.title(f'{feature} Boxplot by Target Class')
        plt.tight_layout()
        plt.show()

    # 准备数据
    x = iris.data
    y = iris.target

    # 划分数据集和训练集
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # 模型训练和预测
    m = SimpleDecisionTree("gini")
    m.fit(X_train, y_train)
    y_predict = m.predict(X_test)
    # print(y_predict)
    # print(y_test.reshape(-1))
    y_predict_accuracy = predict_accuracy(y_predict, y_test.reshape(-1))
    print("决策树准确率：{}".format(y_predict_accuracy))
