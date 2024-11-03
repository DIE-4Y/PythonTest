import torchtext

# train_ds = torchtext.datasets.iMDB('imdb/', train=True, download=True)
# test_ds = torchtext.datasets.iMDB('imdb/', train=False, download=True)

train_iter, test_iter = torchtext.datasets.IMDB()
