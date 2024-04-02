import numpy as np
A = np.loadtxt('univariate.txt', delimiter=',') # Load data from file

# print(A)
print(A[0:4, :]) # Print first 4 rows of A

B= np.savetxt()