'''
1)	Define the following metrics and perform the following operations
i)	Write a Python program using Python Lists
ii)	Write a Python program and NumPy

Matrix A =  [[ 3.7827  3.3454  3.2341]  , [ 2.2122  3.5678  3.9087] , 
[1.1234  2.8934,  5.9087]].

Matrix B =  [[ 3.1234  3.0987  3.1234]  , [ 2.1111  3.2222  3.3333] , 
[1.0987  1.3456,  5.1234]].

Matrix C =  [[ 3.1243  3.0989  3.1256 ]  , [ 2.6721  3.6785  3.9017] , 
[1.1254  2.8956,  5.9187]].
'''

import time
import numpy as np


# Define matrices
matrix_X = [[3.7827, 3.3454, 3.2341], 
            [2.2122, 3.5678, 3.9087], 
            [1.1234, 2.8934, 5.9087]]

matrix_Y = [[3.1234, 3.0987, 3.1234], 
            [2.1111, 3.2222, 3.3333], 
            [1.0987, 1.3456, 5.1234]]

matrix_Z = [[3.1243, 3.0989, 3.1256], 
            [2.6721, 3.6785, 3.9017], 
            [1.1254, 2.8956, 5.9187]]
            

# i)	Write a Python program using Python Lists

def add_matrices_list(X, Y, Z):
    sum_result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            sum_result[i][j] = X[i][j] + Y[i][j] + Z[i][j]
    return sum_result

start_time = time.time()
result_sum = add_matrices_list(matrix_X, matrix_Y, matrix_Z)
end_time = time.time()

time_taken = end_time - start_time
print("Result using lists:", result_sum)
print("Time taken using lists: {:.6f} seconds".format(time_taken))

# Result
''' Result using lists: [[10.0304, 9.543000000000001, 9.4831], [6.9954, 10.4685, 11.143699999999999], [3.3475, 7.1346, 16.9508]]
Time taken using lists: 0.000004 seconds

'''

# ii)	Write a Python program and NumPy


# Matrix addition using NumPy
start_time = time.time()
result_np = matrix_X + matrix_Y + matrix_Z
end_time = time.time()

np_time = end_time - start_time
print("Result using NumPy:", result_np)
print("Time taken using NumPy: {:.6f} seconds".format(np_time))

# Result:
'''
Result using NumPy: [[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087], [3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234], [3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]]
Time taken using NumPy: 0.000001 seconds
'''