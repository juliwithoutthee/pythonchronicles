from tracemalloc import start
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


# Reverse Array in Place (reverse list)
# input: [1,2,3] output: [3,2,1]
def reverse_array(arr):
    start_index = 0
    end_index = len(arr) -1

    while start_index < end_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
    return arr
    

print(reverse_array([1,2,3]))