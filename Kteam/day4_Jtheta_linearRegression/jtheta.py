import numpy as np
from functions import *
raw = np.loadtxt('data.txt', delimiter = ',')
# tạo vector y = cột thứ 3 (index 2) của raw
y = raw[:,0]
# tạo ma trận X trống
X = np.zeros((np.size(y),np.size(raw,1)))
# thêm 1 vào cột đầu
X[:,0] = 1
# thêm 2 cột sau vào
X[:,1:] = raw[:,0:2]
theta = np.array([89597.909542,139.210674 ,-8738.019112])
#bộ theta chính xác là [89597.909542,139.210674 ,-8738.019112]
print(computeCost(X,y,theta),computeCost_Vec(X,y,theta))