class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
    def get_next(self):
        return self.next_node
    def set_next(self, node_object):
        self.next_node = node_object
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
        
        
class LinkedList:
    def __init__(self, root = None):
        self.root = None
        self.size = 0
    def get_size(self):
        return self.size
    def insert_node(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
    def remove_node(self, data):
        previous_node = None
        current_node = self.root
        while current_node != None:
            if current_node.get_data() == data and previous_node != None:
                previous_node.get_next() = current_node.get_next()
                size -= 1
                return True
            #Case when deleting the root
            elif current_node.get_data() == data and previous_node == None:
                self.root = current_node.get_next()
                size -= 1
                return True
            else:
                return False
                
#TestCases
first_Node = Node(5)
second_Node = Node(10, first_Node)
third_Node = Node(15, second_Node)
fourth_Node = Node(20, third_Node)
fifth_Node = Node(25, fourth_Node)
