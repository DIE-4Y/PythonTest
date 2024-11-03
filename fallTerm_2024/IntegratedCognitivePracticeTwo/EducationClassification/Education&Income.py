import torch
import numpy as np
import pandas as pd

data = pd.read_csv("Income1.csv")

print(data)

print(data.info)

print(type(data))

X = torch.from_numpy(data.Education.to_numpy().reshape(-1, 1)).type(torch.FloatTensor)

Y = torch.from_numpy(data.Income.to_numpy().reshape(-1, 1)).type(torch.FloatTensor)

print(X.shape, Y.shape)
print(X, Y)

import matplotlib.pyplot as plt

plt.scatter(data.Education, data.Income)
plt.xlabel('Education')
plt.ylabel('Income')
plt.show()

from torch import nn

class EIModel(nn.Module):
    def __init__(self):
        super(EIModel, self).__init__()
        self.linear = nn.Linear(in_features=1, out_features=1)
    def forward(self, inputs):
        logits = self.linear(inputs)
        return logits

model = EIModel()
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.0001)

for epoch in range(5000):
    for x, y in zip(X, Y):
        y_pred = model(x)
        loss = loss_fn(y_pred, y)
        opt.zero_grad()
        loss.backward()
        opt.step()
print('Down')

print(list(model.named_parameters()))

plt.scatter(data.Education, data.Income, label='real data')
plt.plot(X, model(X).detach().numpy(), c='r', label='predicted line')
plt.xlabel('Education')
plt.ylabel('Income')
plt.legend()
plt.show()

