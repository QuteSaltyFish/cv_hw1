import torch as t 
from torchvision import transforms
from PIL import Image
import numpy as np
class hw1():
    def __init__(self, dir):
        self.DEVICE = t.device("cuda" if t.cuda.is_available() else 'cpu')
        self.img = Image.open(dir)
        self.img_gray = self.img.convert("L")
        self.img_tensor = transforms.ToTensor()(self.img).to(self.DEVICE)
        self.img_gray_tensor = transforms.ToTensor()(self.img_gray).to(self.DEVICE)


    def Roberts(self,gray=True,padding=False):
        Gx = t.tensor([
            [-1.0,0,1],
            [-2,0,2],
            [-1,0,1]
        ]).to(self.DEVICE)
        Gy = t.tensor([
            [1.0,2,1],
            [0,0,0],
            [-1,-2,-1]
        ]).to(self.DEVICE)

        if gray:
            data = self.img_gray_tensor
        else:
            data =  self.img_tensor
            
        if padding:
            data = t.nn.ZeroPad2d(1)(data)
        
        kernal_size=2
        output = t.zeros([data.shape[0],data.shape[1]-kernal_size+1,data.shape[2]-kernal_size+1], dtype=t.float).to(self.DEVICE)
        for k in range(output.shape[0]):
            for i in range(1, data.shape[1]-1):
                for j in range(1, data.shape[2]-1):
                    # print(data[k,i-1:i+1,j-1:j+1])
                    output[k,i,j] = t.abs(t.sum(Gx*data[k,i-1:i+2,j-1:j+2]))+t.abs(t.sum(Gy*data[k,i-1:i+2,j-1:j+2]))

        return transforms.ToPILImage()(output.cpu())



    def Sobel(self,gray=True,padding=False):
        Gx = t.tensor([
            [-1.0,0,1],
            [-2,0,2],
            [-1,0,1]
        ]).to(self.DEVICE)
        Gy = t.tensor([
            [1.0,2,1],
            [0,0,0],
            [-1,-2,-1]
        ]).to(self.DEVICE)

        if gray:
            data = self.img_gray_tensor
        else:
            data =  self.img_tensor
            
        if padding:
            data = t.nn.ZeroPad2d(1)(data)

        kernal_size = 3
        output = t.zeros([data.shape[0],data.shape[1]-kernal_size+1,data.shape[2]-kernal_size+1], dtype=t.float).to(self.DEVICE)
        
        for k in range(output.shape[0]):
            for i in range(0, output.shape[1]-1):
                for j in range(0, output.shape[2]-1):
                    # print(data[k,i-1:i+1,j-1:j+1])
                    output[k,i,j] = t.abs(t.sum(Gx*data[k,i:i+kernal_size,j:j+kernal_size]))+t.abs(t.sum(Gy*data[k,i:i+kernal_size,j:j+kernal_size]))
        return transforms.ToPILImage()(output.cpu())

    def Gaussian(self, kernal_size=5, sigma=1, gray=False, padding=0):
        if gray:
            data = self.img_gray_tensor
        else:
            data =  self.img_tensor

        if padding!=0:
            data = t.nn.ZeroPad2d(padding)(data)
        sum=0
        gaussian = t.zeros([kernal_size, kernal_size], dtype=t.float32).to(self.DEVICE)
        L = (kernal_size+1)//2-1
        for i in range(kernal_size):
            for j in range(kernal_size):
                gaussian[i,j] = np.exp(-1/2 * ((i-L)**2/sigma**2           #生成二维高斯分布矩阵
                                + ((j-L)**2/sigma**2))) / (2*np.pi*sigma*sigma)
                sum = sum + gaussian[i, j]
        # print(gaussian)
        gaussian = gaussian/sum

        output = t.zeros([data.shape[0],data.shape[1]-kernal_size+1,data.shape[2]-kernal_size+1], dtype=t.float).to(self.DEVICE)
        
        for k in range(output.shape[0]):
            for i in range(output.shape[1]):
                for j in range(output.shape[2]):
                    # print(data[k,i-1:i+1,j-1:j+1])
                    output[k,i,j] = t.sum(gaussian*data[k,i:i+kernal_size,j:j+kernal_size])
        return transforms.ToPILImage()(output.cpu())

    def Prewitt(self, gray=True, padding=0):
        Gx = t.tensor([
            [-1.0,0,1],
            [-1,0,1],
            [-1,0,1]
        ]).to(self.DEVICE)
        Gy = t.tensor([
            [1.0,1,1],
            [0,0,0],
            [-1,-1,-1]
        ]).to(self.DEVICE)

        if gray:
            data = self.img_gray_tensor
        else:
            data =  self.img_tensor

        if padding!=0:
            data = t.nn.ZeroPad2d(padding)(data)
            
        kernal_size = 3
        output = t.zeros([data.shape[0],data.shape[1]-kernal_size+1,data.shape[2]-kernal_size+1], dtype=t.float).to(self.DEVICE)
        
        for k in range(output.shape[0]):
            for i in range(0, output.shape[1]-1):
                for j in range(0, output.shape[2]-1):
                    # print(data[k,i-1:i+1,j-1:j+1])
                    output[k,i,j] = t.abs(t.sum(Gx*data[k,i:i+kernal_size,j:j+kernal_size]))+t.abs(t.sum(Gy*data[k,i:i+kernal_size,j:j+kernal_size]))

        return transforms.ToPILImage()(output.cpu())


    def Mean_filter(self, kernal_size=5, sigma=1, gray=False, padding=0):
        if gray:
            data = self.img_gray_tensor
        else:
            data =  self.img_tensor

        if padding!=0:
            data = t.nn.ZeroPad2d(padding)(data)
        
        output = t.zeros([data.shape[0],data.shape[1]-kernal_size+1,data.shape[2]-kernal_size+1], dtype=t.float).to(self.DEVICE)
        
        for k in range(output.shape[0]):
            for i in range(output.shape[1]):
                for j in range(output.shape[2]):
                    # print(data[k,i-1:i+1,j-1:j+1])
                    output[k,i,j] = t.mean(data[k,i:i+kernal_size,j:j+kernal_size])
        return transforms.ToPILImage()(output.cpu())

    def Median_filter(self, kernal_size=5, sigma=1, gray=False, padding=0):
        if gray:
            data = self.img_gray_tensor
        else:
            data =  self.img_tensor

        if padding!=0:
            data = t.nn.ZeroPad2d(padding)(data)
        
        output = t.zeros([data.shape[0],data.shape[1]-kernal_size+1,data.shape[2]-kernal_size+1], dtype=t.float).to(self.DEVICE)
        
        for k in range(output.shape[0]):
            for i in range(output.shape[1]):
                for j in range(output.shape[2]):
                    # print(data[k,i-1:i+1,j-1:j+1])
                    output[k,i,j] = t.median(data[k,i:i+kernal_size,j:j+kernal_size])
        return transforms.ToPILImage()(output.cpu())


if __name__ == "__main__":
    data = hw1('src/img.jpg')
    data.Gaussian(3)