import torch as t 
from torchvision import transforms
from PIL import Image
from func import *


import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


data = hw1('src/img.jpg')
result = data.Gaussian(gray=False,padding=2)
result.save("result/Gaussian.gif")

result = data.Roberts(padding=2)
result.save("result/Roberts.gif")

result = data.Sobel(padding=2)
result.save("result/Sobel.gif")

result = data.Prewitt(padding=2)
result.save("result/Prewitt.gif")

result = data.Mean_filter(kernal_size=3, padding=1)
result.save("result/mean.gif")

result = data.Median_filter(kernal_size=3, padding=1)
result.save("result/Median.gif")

