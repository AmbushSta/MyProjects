'''
Two classes used to create linked lists
Author: Michael Cowie
'''

class Node:
    
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
        
    def set_next(self, node_object):
        self.next_node = node_object
        
    def set_data(self, data):
        self.data = data
        
        
class Linkedlist:
    
    def __init__(self, root = None):
        self.root = None
        self.size = 0
        
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
    
    def find_data(self, data):
        current_index = 0
        current_node = self.root
        while current_node != None:
            if current_node.get_data() == data:
                return current_index
            else:
                current_node = current_node.get_next()
                current_index += 1
                
    def insert_at_index(self, index , data):
        if index == 0:
            self.insert_node(data)
            return True
        if index > self.size:
            return False
        previous_node = None
        current_node = self.root
        for x in range(index):
            previous_node = current_node
            current_node = current_node.get_next()
            if x == index - 1:
                new_node = Node(data, current_node)
                previous_node.set_next(new_node)
                return True
            
    def display_data(self):
        current_node = self.root
        node_number = 0
        while current_node != None:
            print("Node {} has the data {}".format(node_number, current_node.get_data()))
            node_number += 1
            current_node = current_node.get_next()
            
                
#TestCases
'''
myList = Linkedlist()
myList.insert_node(20)
myList.insert_node(15)
myList.insert_node(10)
myList.insert_node(5)
myList.insert_at_index(2,50)
myList.find_data(50)

Correctly displays
Node 0 has the data 5
Node 1 has the data 10
Node 2 has the data 50
Node 3 has the data 15
Node 4 has the data 20
2

All methods and cases have been thurally tested but will
not be all documented on this docstring
'''
