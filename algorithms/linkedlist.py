class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        self.value

class LinkedList: 
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next =Node(value=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            node.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


