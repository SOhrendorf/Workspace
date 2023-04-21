import torch
x = torch.randn(3,5,2)
if torch.cuda.is_available():
    x = x.cuda()
print(x)