import torch
from sklearn.model_selection import train_test_split
from torch import nn
import torch.optim as optim
import numpy as np
import pandas as pd

# 读取数据
data = pd.read_csv('./credit-a.csv', header=None)
print(data)

data = data.apply(pd.to_numeric, errors='coerce')
# 用0替换NaN值，保留所有行
data = data.fillna(0)

# 选择所有行，除了最后一列的所有列
X = data.iloc[:, :-1]
# 选择所有行的最后一列
Y = data.iloc[:, -1]

# 将标签转换为0和1
Y = (Y == 1).astype(int)

# 将数据集分为训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 数据先转化为numpy数据再转化为张量
X_train = torch.from_numpy(X_train.to_numpy().reshape(-1, 15)).float()
X_test = torch.from_numpy(X_test.to_numpy().reshape(-1, 15)).float()
Y_train = torch.from_numpy(Y_train.to_numpy().reshape(-1, 1)).float()
Y_test = torch.from_numpy(Y_test.to_numpy().reshape(-1, 1)).float()

# 将张量转移到GPU
if torch.cuda.is_available():
    X_train = X_train.to('cuda')
    Y_train = Y_train.to('cuda')
    X_test = X_test.to('cuda')
    Y_test = Y_test.to('cuda')


class LogisticRegressionModel(nn.Module):
    # 初始化模型
    def __init__(self):
        super(LogisticRegressionModel, self).__init__()
        # 只定义一层15个输入 1个输出
        self.linear = nn.Linear(in_features=15, out_features=1)

    def forward(self, inputs):
        x = self.linear(inputs)
        """使用sigmoid函数作为输出"""
        return torch.sigmoid(x)


# 确保模型在GPU上运行
model = LogisticRegressionModel().to('cuda')

# 使用BCELoss作为损失函数
loss_fn = nn.BCELoss()
opt = optim.SGD(model.parameters(), lr=0.0001)

# 模型训练
for epoch in range(5000):
    # 将整个训练集当作一个批次进行训练
    model.train()
    # 获取预测值
    y_pred = model(X_train)
    # 计算损失
    loss = loss_fn(y_pred, Y_train)
    # 清空梯度
    opt.zero_grad()
    # 反向传播
    loss.backward()
    # 更新权重
    opt.step()

print('Training complete')

# 测试集评估
with torch.no_grad():
    # 获取测试集的预测值
    y_test_pred = model(X_test)
    # 将概率转换为标签 阈值为0.5
    y_test_pred_labels = (y_test_pred >= 0.5).float()
    # 计算正确预测的数量
    correct = (y_test_pred_labels.squeeze() == Y_test).sum().item()
    # 计算准确率
    accuracy = correct / Y_test.shape[0]

    # 将预测结果与真实结果组成DataFrame
    results_df = pd.DataFrame({
        'True Label': Y_test.cpu().numpy().squeeze(),
        'Predicted Label': y_test_pred_labels.cpu().numpy().squeeze(),
        'Predicted Probability': y_test_pred.cpu().numpy().squeeze()
    })

print(f'Test Accuracy: {accuracy:.4f}')
# 打印前五个预测结果与真实结果的对比
print(results_df.head(20))
