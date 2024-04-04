import numpy as np
import matplotlib.pyplot as plt
#! load data from file *.txt
#* np.loadtxt(fname, dtype, delimiter)
# A = np.loadtxt('univariate.txt', delimiter=',')
# print(A)
# print(A[0:4, :]) # Print first 4 rows of A
#$\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$#
#! save data from file *.txt
#* np.savetxt(fname, X, fmt, delimiter)
# A = [ [ 1, 2 ], [ 3, 4 ] ] #create a 2*2 matrix
# np.savetxt('Saved_A.txt', A, fmt = '%.2f', delimiter = ',') #save A to Saved_A.txt
#$\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$#
# #! h_theta(x) to predict output with availavle theta
#import toàn bộ file univariate.txt
X = np.loadtxt('univariate.txt', delimiter = ',')
#import Theta từ file univariate_theta.txt
Theta = np.loadtxt('univariate_theta.txt')
# $\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$#
#Lưu cột y
y = np.copy(X[:,-1])
#Chuyển cột đầu (x1) sang cột thứ 2
X[:,1] = X[:,0]
#Đổi cột đầu thành số 1
X[:,0] = 1
#$\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$#
#Tính lợi nhuận (đơn vị 10000$)
predict = X @ Theta
#Chuyển lợi nhuận về đơn vị $
predict = 10000 * predict
#in cặp dân số-lợi nhuận đầu tiên (đơn vị dân số: người)
print('%d người : %.2f$' %(X[0,1]*10000,predict[0]))
#Lưu kết quả
np.savetxt('predicted_value.txt',predict,fmt = '%.6f')
#Plot giá trị thực tế (không lấy cột bias 1 đầu)
#X[:,1:] là x-axis của biểu đồ, không lấy cột đầu; y là y-axis, rx là red x, plot dữ liệu bằng dấu x màu đỏ
plt.plot(X[:,1:],y,'rx')
#Plot dự đoán
plt.plot(X[:,1:],predict/10000,'-b')#ta dùng đơn vị gốc là 10000$, -b là đường thẳng màu xanh
#show kết quả
plt.show()
#Lưu kết quả
np.savetxt('predicted_value.txt',predict,fmt = '%.6f')