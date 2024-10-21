import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 读取CSV文件
df = pd.read_csv('stuInform.csv')

# 特征缩放
scaler = StandardScaler()
features = df[['age', 'height(cm)', 'weight(kg)']]
scaled_features = scaler.fit_transform(features)

n_neighbors = [3, 5, 7, 9, 11, 13]
for i in n_neighbors:
    accuracies = 0.0
    for k in range(100):

        # 创建训练集和测试集
        X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['gender'], test_size=0.2)

        # 模型创建与训练
        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X_train, y_train)

        # 进行预测
        y_pred = knn.predict(X_test)

        # 评估模型准确性
        accuracy = accuracy_score(y_test, y_pred)
        # print(f'n = {i} Model Accuracy: {accuracy}')
        accuracies += accuracy
    print(f'n = {i} Model Accuracy: {accuracies/100}')


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score
#
# # 读取CSV文件
# df = pd.read_csv('stuInform.csv')
#
# # 特征缩放
# scaler = StandardScaler()
# features = df[['height(cm)', 'weight(kg)']]
# scaled_features = scaler.fit_transform(features)
#
# n_neighbors = [3, 5, 7, 9]
# for i in n_neighbors:
#     accuracies = 0.0
#     for k in range(100):
#
#         # 创建训练集和测试集
#         X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['gender'], test_size=0.2)
#
#         # 模型创建与训练
#         knn = KNeighborsClassifier(n_neighbors=3)
#         knn.fit(X_train, y_train)
#
#         # 进行预测
#         y_pred = knn.predict(X_test)
#
#         # 评估模型准确性
#         accuracy = accuracy_score(y_test, y_pred)
#         # print(f'n = {i} Model Accuracy: {accuracy}')
#         accuracies += accuracy
#     print(f'n = {i} Model Accuracy: {accuracies/100}')
