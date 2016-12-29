class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
    def get_next(self):
        return self.next_node
    def set_next(self, node_object):
        self.next_node = node_object
    def get_data(self):
        self.data
    def set_data(self, data):
        self.data = data
        
firstNode = Node(5)
secondNode = Node(10, firstNode)
