import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
import torchvision
from torchvision import transforms

# 设置训练集和数据集相对的地址
train_dir = r'class_2/train'
test_dir = r'class_2/test'

# 数据预处理 转为tensor张量 归一化
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# 载入数据集
train_ds = torchvision.datasets.ImageFolder(
    train_dir, transform=transform
)

test_ds = torchvision.datasets.ImageFolder(
    test_dir, transform=transform
)

# 打印标签 {'airplane': 0, 'lake': 1}
print(train_ds.classes)
# 打印数据标签对应字典 {'airplane': 0, 'lake': 1}
print(train_ds.class_to_idx)
print(len(train_ds), len(test_ds))

# 设置训练块
BATCHSIZE = 16
train_dl = torch.utils.data.DataLoader(
    train_ds, batch_size=BATCHSIZE, shuffle=True
)
test_dl = torch.utils.data.DataLoader(
    test_ds, batch_size=BATCHSIZE
)

# 获取一个批次的数据
imgs, labels = next(iter(train_dl))

print(imgs.shape)
print(imgs[0].shape)

# 将张量转化为ndarray数据
im = imgs[0].permute(1, 2, 0).numpy()
print(im.max(), im.min())

# 再次将范围回到0-1
im = (im + 1) / 2

# 打印第一张图片
plt.title(labels[0].item())
plt.imshow(im)
plt.show()

# 将字典反转变为 {0: 'airplane', 1: 'lake'}
id_to_class = dict((v, k) for k, v in train_ds.class_to_idx.items())
print(id_to_class)

# 依照批次绘制前六张图片
plt.figure(figsize=(12, 8))
for i, (img, label) in enumerate(zip(imgs[:6], labels[:6])):
    img = (img.permute(1, 2, 0).numpy() + 1) / 2
    plt.subplot(2, 3, i + 1)
    plt.title(id_to_class.get(label.item()))
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img)
    plt.show()


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, 3)
        self.conv3 = nn.Conv2d(32, 64, 3)
        self.fc1 = nn.Linear(64 * 30 * 30, 1024)
        self.fc2 = nn.Linear(1024, 128)
        self.fc3 = nn.Linear(128, 2)

    def forward(self, x):
        X = self.pool(F.relu(self.conv1(x)))
        X = self.pool(F.relu(self.conv2(X)))
        X = self.pool(F.relu(self.conv3(X)))
        X = X.view(-1, 64 * 30 * 30)
        X = F.relu(self.fc1(X))
        X = F.relu(self.fc2(X))
        X = self.fc3(X)
        return X


device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device " + device)
model = Net().to(device)
pred = model(imgs.to(device))

print("imgs.shape" + str(imgs.shape))
print("pred.shape" + str(pred.shape))
print(torch.argmax(pred, 1))

loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.005)


def train(dataloader, model, loss_fn, optimiser):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    train_loss, correct = 0, 0
    for X, y in dataloader:
        X, y = X.to(device), y.to(device)
        pred = model(X)
        loss = loss_fn(pred, y)
        optimiser.zero_grad()
        loss.backward()
        optimiser.step()

        with torch.no_grad():
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
            train_loss += loss.item()
    train_loss /= num_batches
    correct /= size
    return train_loss, correct


def test(dataloader, model):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
        test_loss /= num_batches
        correct /= size
        return test_loss, correct


epochs = 50

train_loss = []
train_accuracy = []
test_loss = []
test_accuracy = []

for epoch in range(epochs):
    epoch_loss, epoch_accuracy = train(train_dl, model, loss_fn, optimizer)
    epoch_test_loss, epoch_test_accuracy = test(test_dl, model)
    train_loss.append(epoch_loss)
    train_accuracy.append(epoch_accuracy)
    test_loss.append(epoch_test_loss)
    test_accuracy.append(epoch_test_accuracy)

    template = ("epoch:{:2d}, train_loss:{:.4f}, train_accuracy:{:.2f}%,"
                " test_loss:{:.4f}, test_accuracy:{:.2f}%")
    print(template.format(
        epoch, epoch_loss, epoch_accuracy * 100, epoch_test_loss, epoch_test_accuracy * 100
    ))

print("Done!")

plt.plot(range(1, epochs + 1), train_loss, label="Train Loss")
plt.plot(range(1, epochs + 1), test_loss, label="Test Loss", ls="--")
plt.legend()
plt.show()

plt.plot(range(1, epochs + 1), train_accuracy, label="Train Accuracy")
plt.plot(range(1, epochs + 1), test_accuracy, label="Test Accuracy", ls="--")
plt.legend()
plt.show()
