
class Node:
    def __init__(self,data):
        self.left = None        # create left node
        self.right = None       # create right node
        self.data = data


    def insert(self,data):
        if self.data:

            # if the inserted element is less than the node element
            # insert the element on the left of the node
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            
            # if the inserted element is greater than the node element
            # insert the element on the right of the node        
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data


    # print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()



# driver code
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(2)
root.insert(23)

print('Traversing the Binary Tree:-')
print('*'*28)
root.print_tree()
print('*'*28)