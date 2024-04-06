import sys
sys.path.append('../day4_Jtheta_linearRegression')
from functions import *
def GradientDescent(X,y,alpha = 0.02, iter=5000):#giá trị mặc định của alpha là 0.02, iter (số vòng lặp tối đa) là 5000
    #Giá trị ban đầu của theta = 0
    theta = np.zeros(np.size(X,1)) #số lượng theta bằng số cột của X
    #array lưu lại các giá trị J trong quá trình lặp
    J_hist = np.zeros((iter,2)) # kích thước là iter*2, cột đầu chỉ là các số từ 1 đến iter để tiện cho việc plot. Kích thước được truyền vào qua một tupple
    #kích thước của training set
    m = np.size(y)
    #ma trận ngược (đảo hàng và cột) của X
    X_T = np.transpose(X)
    #biến tạm để kiểm tra tiến độ Gradient Descent
    pre_cost = computeCost(X,y,theta)

