net = IDN(parameters)
from torchsummaryX import summary
summary(net,torch.zeros((1,3,320,180)))