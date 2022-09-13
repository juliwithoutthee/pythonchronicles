

# Using a max heap, sort any list
# input visualization tree 
#       5   
#   16      8
# 14  20  1  26

input = [5, 16, 8, 14, 20, 1, 26]
output = [1, 5, 8, 14, 16, 20, 26]

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def siftDown(lst, i, upper):
    while(True):
        l, r = i*2+1, i*2+2
        if max(l, r) < upper:
            if lst[i] >= max(lst[l], lst[r]): break
            elif lst[l] > lst[r]:
                swap(lst, i, l)
                i = l 
            else: 
                swap(lst, i, r)
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst, i, l)
                i = l
            else: break 
        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst, i, r)
                i = r
            else: break
        else: break


def heapsort(lst):
    # heapify into Max Heap
    # sort the list 
    for j in range((len(lst)-2)//2, -1, -1):
        siftDown(lst, j, len(lst))
    
    for end in range(len(lst)-1, 0, -1):
        swap(lst, 0, end)
        siftDown(lst, 0, end)


print(input)
heapsort(input)
print(input)





# Use min heap below
test_list = [15, 8, 3, 7, 2, 5, 0, 4, 1, 20]
test_output = [0, 1, 2, 3, 4, 5, 7, 8, 15, 20]