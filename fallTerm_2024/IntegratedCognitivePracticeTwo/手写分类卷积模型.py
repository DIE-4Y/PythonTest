import torch
import torchvision
from torch.utils.data import dataloader
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import numpy as np
from torch import nn
from torch.optim import SGD

train_ds = torchvision.datasets.MNIST('data/',
                                      train=True, transform=ToTensor(), download=True)

test_ds = torchvision.datasets.MNIST('data/',
                                     train=False, transform=ToTensor(), download=True)

train_dl = torch.utils.data.DataLoader(train_ds, batch_size=64, shuffle=True)

test_dl = torch.utils.data.DataLoader(test_ds, batch_size=64)

imgs, labels = next(iter(train_dl))
print(imgs.shape)
print(labels.shape)

# plt.figure(figsize=(10, 1))
# for i, img in enumerate(imgs[:10]):
#     npimg = img.numpy()
#     npimg = np.squeeze(npimg)
#     plt.subplot(1, 10, i + 1)
#     plt.imshow(npimg)
#     plt.axis('off')
#
# print(labels[:10])

# input = torch.randn(20, 3, 256, 256)
# print(input)
# output = torch.relu(input)
# print(output)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)

        self.linear1 = nn.Linear(16 * 4 * 4, 120)
        self.linear2 = nn.Linear(120, 10)

    def forward(self, input):
        X = torch.max_pool2d(torch.relu(self.conv1(input)), 2)
        X = torch.max_pool2d(torch.relu(self.conv2(X)), 2)
        X = X.view(-1, 16 * 4 * 4)
        X = torch.relu(self.linear1(X))
        X = self.linear2(X)
        return X


loss_fn = nn.CrossEntropyLoss()

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device: ", device)
model = Model().to(device)
optimiser = SGD(model.parameters(), lr=0.01)


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
    epoch_loss, epoch_accuracy = train(train_dl, model, loss_fn, optimiser)
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

plt.plot(range(1, epochs + 1), train_accuracy, label="Train Loss")
plt.plot(range(1, epochs + 1), test_accuracy, label="Test Loss", ls="--")
plt.xlabel("Epochs")
plt.legend()
plt.show()
