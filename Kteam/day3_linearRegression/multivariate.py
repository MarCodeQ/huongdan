import numpy as np

#! Đầu tiên, chúng ta sẽ load cả 2 file:
#import toàn bộ file multivariate.txt
_X = np.loadtxt('multivariate.txt', delimiter = ',')
#import Theta từ file multivariate_theta.txt
Theta = np.loadtxt('multivariate_theta.txt')
# $\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$#
#! Bước tiếp theo, chúng ta sẽ xóa cột kết quả thực tế và thêm cột x0 = 1 vào đầu.
#Tạo ma trận X bằng kích thước của _X
X = np.zeros((np.size(_X,0),np.size(_X,1)))
#Thêm cột đầu bằng 1
X[:,0] = 1
#Thêm các cột x1 -> xn
n = np.size(_X,1) - 1
X[:,1:] = _X[:,0:n]
# $\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$#
#!Các bước sau như dự đoán kết quả, in kết quả, lưu kết quả hoàn toàn giống với univariate problem.
#Tính giá nhà (đơn vị $)
predict = X @ Theta
#in bộ diện tích-số phòng-giá đầu tiên
print('%.2f feet-vuông, %d phòng ngủ : %.1f$' %(X[0,1], X[0,2], predict[0]))

#Lưu kết quả
np.savetxt('predicted_value.txt',predict,fmt = '%.2f')
