
class Node: 
    def __init__(self, value):
        self.left = None 
        self.right = None 
        self.value = value

    def traversePreOrder(self):
        print(self.value, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.value, end=' ')
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left: 
            self.left.traversePostOrder()
        if self.right: 
            self.right.traversePostOrder()
        print(self.value, end=' ')

root = Node(1)

root.left = Node(2)
root.right = Node(3)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()



class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right

    def search(searchValue, node):
        if node is None or node.value == searchValue:
            return node
        elif searchValue < node.value:
            return TreeNode.search(searchValue, node.leftChild)
        else: 
            return TreeNode.search(searchValue, node.rightChild)