from function import *
from torchvision import transforms
import torch as t 
import numpy
data = hw1('src/img.jpg')
result = transforms.ToPILImage(data.Roberts())
result.show()