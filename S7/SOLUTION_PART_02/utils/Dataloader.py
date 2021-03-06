import torch
import torchvision
import torchvision.transforms as transforms

def train_test_loader(batch_size,num_workers):
  train_transform = transforms.Compose(
  [transforms.ToTensor(),
  transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
  ])
  test_transform = transforms.Compose(
  [transforms.ToTensor(),
  transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
  ])

  train = torchvision.datasets.CIFAR10('./data', train=True, download=True, transform=train_transform)
  test = torchvision.datasets.CIFAR10('./data', train=False, download=True, transform=test_transform)
  SEED = 1
  # CUDA?
  cuda = torch.cuda.is_available()
  print("CUDA Available?", cuda)
  # For reproducibility
  torch.manual_seed(SEED)
  if cuda:
      torch.cuda.manual_seed(SEED)
  # dataloader arguments - something you'll fetch these from cmdprmt
  dataloader_args = dict(shuffle=True, batch_size=batch_size, num_workers=num_workers, pin_memory=True) if cuda else dict(shuffle=True, batch_size=Args.batch_size)
  # train dataloader
  trainloader = torch.utils.data.DataLoader(train, **dataloader_args)
  # test dataloader
  testloader = torch.utils.data.DataLoader(test, **dataloader_args)
  return trainloader,testloader

def get_classes():
  classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
  return classes
    