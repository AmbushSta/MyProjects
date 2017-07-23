class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
#My binary tree implementation does not allow duplicates        
class Tree():
    def __init__(self):
        self.root = None
    
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.add_helper(value, self.root)
            
    #Recursive method reaching all nodes     
    def add_helper(self, value, node):
        #Check left node
        if value < node.value:
            #Check if it is a leaf node
            if node.left is None:
                node.left = Node(value)
            else:
                self.add_helper(value, node.left)
        #Check right node        
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.add_helper(self, value, node.right)
                
    def print_tree(self):
        if self.root != None:
            bfs = self.bfs_traversal(self.root)
            print(bfs)
            #incomplete print of tree
            
    def bfs_traversal(self, node):
        traversal_order = []
        queue = [node]
        while len(queue) != 0:
            node_popped = queue.pop(0)
            if node_popped != None:
                traversal_order.append(node_popped.value)
                queue.append(node_popped.left)
                queue.append(node_popped.right)
        return traversal_order

                   
tree = Tree()
tree.add(5)
tree.add(3)
tree.add(1)
tree.add(7)
tree.add(4)
tree.print_tree()
