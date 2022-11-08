import numpy as np 

random_int = np.random.randint(1,100)
print(random_int)


new_array = np.arange(0,10,2)
print(new_array)

# creates an array in a matrix format 
new_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(new_matrix)

# 5x5 matrix of zeros 
zero_matrix = np.zeros((5,5))
print(zero_matrix)


# Create an array with values from 10-50
ten_to_fifty = np.arange(10,51)
print(ten_to_fifty)
#array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
#       44, 45, 46, 47, 48, 49, 50])

ten_to_fifty[ten_to_fifty%2 == 0] # array of even numbers from 10-50

print(np.arange(10,51,2))

# create the output array:  array([ 5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.])
arr_fives = np.ones(10) * 5
print(arr_fives)


matrix = mat = np.arange(1,26).reshape(5,5)

print(matrix.sum())