import numpy as np 


# not a real array, real arrays do not exist in Python
array = [10, 2, 8, 5, 101, 55]

print(array[:-1])

max = array[0]

for num in array: 
    if num > max:
        max = num

print(max)  # O(n) linear search

min = array[0]

for num in array:
    if num < min:
        min = num

print(min)  # O(n) linear search

# Numpy allows for faster runtimes with a numpy array
numpy_array = np.array(array)

print(numpy_array)
