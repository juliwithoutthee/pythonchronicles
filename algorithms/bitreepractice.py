# pointer to root of binary tree and two values v1 v2
# return the lowest common ancestor of v1 and v2 in binary search tree 
# v1 v2 are int and exist in the tree 
# Check for null? 
# No duplicate numbers 
# -1000 < n < 1000, where n is node.value
# Depth First Search 
# size of the tree is n 
# time complexity 


class Solution: 
    def __init__(self) -> None:
        pass


def lca(nodeRoot, v1, v2):
    if(v1 < nodeRoot and v2 > nodeRoot) or (v2 < nodeRoot and v1 > nodeRoot):
        return Node.getLevel()
    return 0 # default return?

# check how to write this node in python
class Node:
    lvl = 0
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self, node):
        return self.value 
    
    def getLevel(self, v1, v2):
        self