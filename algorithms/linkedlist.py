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

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return 
        for current_node in self:
            pass 
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None: 
            raise Exception("List is Empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node 
                return 

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None: 
            raise Exception("List is Empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head
        for node in self: 
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return 
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    
