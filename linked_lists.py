'''
Two classes used to create linked lists
Author: Michael Cowie
'''

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
        
        
class Linkedlist:
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
            if current_node.get_data() == data:
                if previous_node != None:
                    previous_node.set_next(current_node.get_next())
                else:
                    self.root = current_node.get_next()
                self.size -= 1
                return True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
        return False
    def display_data(self):
        current_node = self.root
        node_number = 0
        while current_node != None:
            print("Node number {} has the data {}".format(node_number, current_node.get_data()))
            node_number += 1
            current_node = current_node.get_next()
            
                
#TestCases
myList = Linkedlist()
myList.insert_node(20)
myList.insert_node(15)
myList.insert_node(10)
myList.insert_node(5)


'''
myList.display_data()
myList.remove_node(15)
myList.display_data()

Correctly removes node with data 15
'''
