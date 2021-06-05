class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def Insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.Insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else: 
                    self.right.Insert(data)
        else:
            self.data = data            
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end=" ")
        if self.right:
            self.right.PrintTree()

root = Node(8)
root.Insert(6)
root.Insert(7)
root.Insert(9)
root.Insert(10)
root.PrintTree()
print("\n")
