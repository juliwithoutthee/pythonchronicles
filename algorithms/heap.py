import heapq

H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
# Sorts the array through heapify
print(H)


# Given an array return the k-th smallest number 
# Duplicates are possible 
# n = len of array 
# k <= n 

def k_smallest_in_array(inputArray, k):
    sortedArr = heapq.heapify(inputArray)
    for i in range(1, k-1):
        smallest = heapq.heappop(sortedArr) #rewrite
    return smallest

# sort the array 
# get the smallest