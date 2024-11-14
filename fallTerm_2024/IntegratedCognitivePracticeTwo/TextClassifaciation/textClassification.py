import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchtext.data.functional import to_map_style_dataset
import torchtext
from torchtext.data.utils import get_tokenizer  # 分词工具
from torchtext.vocab import build_vocab_from_iterator  # 创建词表工具

train_iter, test_iter = torchtext.datasets.IMDB('./data/')
tokenizer = get_tokenizer('basic_english')  # 分词工具做初始化


def yield_tokens(data):
    for _, text in data:
        yield tokenizer(text)


vocab = build_vocab_from_iterator(yield_tokens(train_iter), specials=["<pad>", "<unk>"])
vocab.set_default_index(vocab["<unk>"])
vocab(['this', 'is', 'a', 'book', 'about', 'pytorch'])
text_pipeline = lambda x: vocab(tokenizer(x))
label_pipeline = lambda x: int(x == 'pos')
text_pipeline('this is a book about pytorch')
label_pipeline('pos')
label_pipeline('neg')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def collate_batch(batch):
    label_list, text_list, offsets = [], [], [0]
    for (_label, _text) in batch:
        label_list.append(label_pipeline(_label))
        precess_text = torch.tensor(text_pipeline(_text), dtype=torch.int64)
        text_list.append(precess_text)
        offsets.append(precess_text.size(0))
    label_list = torch.tensor(label_list)
    text_list = torch.cat(text_list)
    offsets = torch.tensor(offsets[:-1]).cumsum(dim=0)
    return label_list.to(device), text_list.to(device), offsets.to(device)


train_dataset = to_map_style_dataset(train_iter)
test_dataset = to_map_style_dataset(test_iter)

train_dataloader = DataLoader(train_dataset, batch_size=64,
                              shuffle=True, collate_fn=collate_batch)
test_dataloader = DataLoader(test_dataset, batch_size=64,
                             shuffle=True, collate_fn=collate_batch)


# 创建模型
class TextClassificationModel(nn.Module):

    def __init__(self, vocab_size, embed_dim, num_class):
        super(TextClassificationModel, self).__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, embed_dim, sparse=True)
        self.fc = nn.Linear(embed_dim, num_class)
        self.init_weights()

    def init_weights(self):
        initrange = 0.5
        self.embedding.weight.data.uniform_(-initrange, initrange)
        self.fc.weight.data.uniform_(-initrange, initrange)
        self.fc.bias.data.zero_()

    def forward(self, text, offsets):
        embedded = self.embedding(text, offsets)
        return self.fc(embedded)


num_class = 2

vocab_size = len(vocab)
emsize = 100
model = TextClassificationModel(vocab_size, emsize, num_class).to(device)

loss_fn = nn.CrossEntropyLoss()
from torch.optim import lr_scheduler

optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
exp_lr_scheduler = lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)


def train(dataloader):
    total_acc, total_count, total_loss, = 0, 0, 0
    model.train()
    for label, text, offsets in dataloader:
        predited_label = model(text, offsets)
        loss = loss_fn(predited_label, label)
        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            total_acc += (predited_label.argmax(1) == label).sum().item()
            total_count += label.size(0)
            total_loss += loss.item() * label.size(0)
    return total_loss / total_count, total_acc / total_count


def test(dataloader):
    model.eval()
    total_acc, total_count, total_loss, = 0, 0, 0

    with torch.no_grad():
        for idx, (label, text, offsets) in enumerate(dataloader):
            predited_label = model(text, offsets)
            loss = loss_fn(predited_label, label)
            total_acc += (predited_label.argmax(1) == label).sum().item()
            total_count += label.size(0)
            total_loss += loss.item() * label.size(0)
    return total_loss / total_count, total_acc / total_count


def fit(epochs, train_dl, test_dl):
    train_loss = []
    train_acc = []
    test_loss = []
    test_acc = []

    for epoch in range(epochs):
        epoch_loss, epoch_acc = train(train_dl)
        epoch_test_loss, epoch_test_acc = test(test_dl)
        train_loss.append(epoch_loss)
        train_acc.append(epoch_acc)
        test_loss.append(epoch_test_loss)
        test_acc.append(epoch_test_acc)
        exp_lr_scheduler.step()
        template = ("epoch:{:2d}, train_loss: {:.5f}, train_acc: {:.1f}% ,"
                    "test_loss: {:.5f}, test_acc: {:.1f}%")
        print(template.format(
            epoch, epoch_loss, epoch_acc * 100, epoch_test_loss, epoch_test_acc * 100))
    print("Done!")

    return train_loss, test_loss, train_acc, test_acc


EPOCHS = 30

train_loss, test_loss, train_acc, test_acc = fit(EPOCHS, train_dataloader, test_dataloader)