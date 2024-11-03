import glob

import matplotlib.pyplot as plt
import torch
from PIL import Image
from torch import nn
from torch.utils import data
from torchvision.transforms import transforms
from torch.nn import functional as F

# 设置图片路径和类别
imgs = glob.glob("dataset2/*.jpg")
species = ['cloudy', 'rain', 'shine', 'sunrise']

# 设置图片类别与标签对应 {'cloudy': 0, 'rain': 1, 'shine': 2, 'sunrise': 3}
species_to_idx = dict((c, i) for i, c in enumerate(species))
# print(species_to_idx)
# 将字典反序 {0: 'cloudy', 1: 'rain', 2: 'shine', 3: 'sunrise'}
idx_to_species = dict((v, k) for k, v in species_to_idx.items())
# print(idx_to_species)

# 提取列表的标签
labels = []
for img in imgs:
    for i, c in enumerate(species):
        if c in img:
            labels.append(i)
# print(labels[:4])

# 图片预处理
transform = transforms.Compose([
    transforms.Resize((96, 96)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])


class WT_dataset(data.Dataset):
    def __init__(self, imgs_path, labels):
        self.imgs_path = imgs_path
        self.labels = labels

    def __getitem__(self, index):
        imgs_path = self.imgs_path[index]
        lable = self.labels[index]
        pil_img = Image.open(imgs_path).convert("RGB")
        pil_img = transform(pil_img)
        return pil_img, lable

    def __len__(self):
        return len(self.imgs_path)


dataset = WT_dataset(imgs, labels)
count = len(dataset)
# print(count)

train_count = int(0.8 * count)
test_count = count - train_count
train_dataset, test_dataset = data.random_split(dataset,
                                                [train_count, test_count])
# print(len(train_dataset), len(test_dataset))
BATCH_SIZE = 16
train_dl = torch.utils.data.DataLoader(
    train_dataset, batch_size=BATCH_SIZE, shuffle=True
)
test_dl = torch.utils.data.DataLoader(
    test_dataset, batch_size=BATCH_SIZE
)

imgs_batch, labels_batch = next(iter(train_dl))


# plt.figure(figsize=(12, 8))
# for i, (img, label) in enumerate(zip(imgs_batch[:6]), labels_batch[:6]):
#     img = (img.permute(1, 2, 0).numpy() + 1) / 2
#     plt.subplot(2, 3, i + 1)
#     plt.title(idx_to_species.get(label.item()))
#     plt.imshow(img)
#     plt.show()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3)
        self.conv2 = nn.Conv2d(16, 32, 3)
        self.conv3 = nn.Conv2d(32, 64, 3)
        self.fc1 = nn.Linear(64 * 10 * 10, 1024)
        self.fc2 = nn.Linear(1024, 4)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, 2)
        x = x.view(-1, 64 * 10 * 10)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


device = "cuda" if torch.cuda.is_available() else "cpu"
model = Net().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


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
plt.xlabel("Epochs")
plt.legend()
plt.show()

plt.plot(range(1, epochs + 1), train_accuracy, label="Train Accuracy")
plt.plot(range(1, epochs + 1), test_accuracy, label="Test Accuracy", ls="--")
plt.xlabel("Epochs")
plt.legend()
plt.show()
