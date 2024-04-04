import numpy as np

#! Initialize a vector
#* Object: A list or a tuple
#* dtype: Data type of the vector
#* ndmin: Minimum number of dimensions of the vector
#$ Exept Object, every parameter needs key_argument
np.array(object, dtype=None, ndmin=0)
__3_dimsquare_matrix = [[1,2,3],[4,5,6],[7,8,9]]
_3_dimsquare_matrix = np.array(__3_dimsquare_matrix)
#@ print(_3_dimsquare_matrix)
#$/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/#
#! Access elements of a vector
#* Matrix_name[row_index, column_index]
__2_dimsquare_matrix = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ] #array-like object
_2_dimsquare_matrix = np.array(__2_dimsquare_matrix) #create a 2-dimension array (matrix) from _a
# print('a:\n',a) #print a
# print('a[0, 1]:', a[0, 1]) #print a[0, 1] elements
# print('a[:, 0]:', a[:, 0]) #print a[:, 0] elements
# print('a[1, :]:', a[1, :]) #print a[1, :] elements
#$/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/#
#! Multiply a matrix with a vector
#* Matrix_name.dot(vector)
#* Matrix @ vector
#$/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/#
#! Multiply two vectors
#* Matrix1.dot(matrix2)
#* Matrix1 @ matrix2
#$/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/#
#! Entity matrix
#* np.eye(dim)
a = np.eye(5)
# print(a)
print(a == 1)
#$/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/#
#! Inverese matrix
#*  np.linalg.pinv(matrix)
_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
a = np.array(_a)
a_i = np.linalg.pinv(a) #Create inverse of a
print(a_i)
print(a @ a_i)
#$/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/#
#! Transpose matrix
#* Matrix_name.T
_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
a = np.array(_a)
a_t = np.transpose(a) #Create transpose of a
print(a)
print(a_t)
#$/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/#
#! Size of a matrix
#* np.size(matrix, axis)
#& axis = None: number of elements
#& axis = 0: number of rows
#& axis = 1: number of columns
_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
a = np.array(_a)
print(np.size(a))
print(np.size(a, 0))
print(np.size(a, 1))
#$/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/#
#!sum max/min of a matrix
#* np.sum(matrix, axis)
#* np.max(matrix, axis)
#* np.min(matrix, axis)
_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
a = np.array(_a)
print(np.sum(a, 0))
print(np.max(a))
print(np.min(a, 1))