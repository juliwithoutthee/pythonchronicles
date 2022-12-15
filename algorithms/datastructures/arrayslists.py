from tracemalloc import start
import numpy as np 


# not a real array, real arrays do not exist in Python
array = [10, 2, 8, 5, 101, 55]

print(array[:-1])

max = array[0]

for num in array: 
    if num > max:
        max = num

# print(max)  # O(n) linear search

min = array[0]

for num in array:
    if num < min:
        min = num

# print(min)  # O(n) linear search

# Numpy allows for faster runtimes with a numpy array
numpy_array = np.array(array)

# print(numpy_array)


# Reverse in Place (reverse list) O(n)
# input: [1,2,3] output: [3,2,1]
def reverse_lst(lst):
    start_index = 0
    end_index = len(lst) -1

    while start_index < end_index:
        # swap items simultaneously 
        lst[start_index], lst[end_index] = lst[end_index], lst[start_index] 
        start_index = start_index + 1
        end_index = end_index - 1

    return lst


# print(reverse_lst([1,2,3]))
# print(reverse_lst("dog"))


# Palindrome - check if the string is a palindrome 
# input: racecar output: true  input:dog output: false 
def is_palindrome(string):
    if string == string[::-1]:
        return True
    
    return False
    


# print(is_palindrome("dog"))
# print(is_palindrome("racecar"))

def check_palindrome(s):
    # iterate and check if the values are the same in place 
    start = 0
    end = len(s)-1
    status = True
    while start < end:
            if(s[start] == s[end]):
                start += 1
                end -= 1
            else: 
                status = False
                break
    return status


# print(check_palindrome("yooo"))
# print(check_palindrome("dad"))

# input: 1234 output: 4321
def reverse_int(num):
    str_num = str(num) 
    return int(str_num[::-1])

# print(reverse_int(1234))

def reverse_integer(n):
    reversed_int = 0
    remainder = 0 
    
    while n > 0:
        remainder = n % 10 
        reversed_int = reversed_int*10 + remainder
        n = n // 10
    return reversed_int

# print(reverse_integer(4321))


# inputs : "restful" "fluster" output: true 
# check if two strings are anagrams 
# logarithmic time complexity O(n log n)
def is_anagram(s1, s2):
    # put amount of characters into dictionary and compare? 
    if len(s1) != len(s2):
        return False 
    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False 

    return True

# print(is_anagram("restful", "fluster"))
# print(is_anagram("dog", "cats"))

# dutch flag sorting problem linear 
def dutch_flag_problem(nums, pivot=1):
    i = 0
    j = 0
    k = len(nums) - 1

    while j <= k:
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] > pivot: 
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
        else: 
            j += 1
    return nums


# def swap(lst, index1, index2):
#     lst[index1], lst[index2] = lst[index2], lst[index1]
#     return lst
print(dutch_flag_problem([1,1,0,2]))

# example list comprehension for Garrett 
arr1 = [0, 1, 2, 5, 6]
arr_comp = [x*10 for x in arr1]
