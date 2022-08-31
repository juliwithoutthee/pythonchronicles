
from tomlkit import value


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

    def insert(value, node):
        if value < node.value:
            if node.leftChild is None:
                node.leftChild = TreeNode(value)
            else:
                TreeNode.insert(value, node.leftChild)
        elif value > node.value:
            if node.rightChild is None:
                node.rightChild = TreeNode(value)
            else: 
                TreeNode.insert(value, node.rightChild)

    def delete(valueToDelete, node):
        if node is None:
            return None
        elif valueToDelete < node.value:
            node.leftChild = TreeNode.delete(valueToDelete, node.leftChild)
            return node
        elif valueToDelete == node.value:
            if node.leftChild is None: 
                return node.rightChild
            elif node.rightChild is None:
                return node.leftChild
            else: 
                node.rightChild = TreeNode.lift(node.rightChild, node)
                return node

    def lift(node, nodeToDelete):
        if node.leftChild:
            node.leftChild = TreeNode.lift(node.leftChild, nodeToDelete)
            return node
        else: 
            nodeToDelete.value = node.value
            return node.rightChild
