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
        
    def findval(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " not found"
            return self.left.findval(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " not found"
            return self.right.findval(value)
        else:
            print(str(self.data) + " found")
    def Print(self):
        if self.left:
            self.left.Print()
        print(self.data)
        if self.right:
            self.right.Print()

root = Node(5)
root.Insert(3)
root.Insert(4)
root.Insert(6)
root.Insert(7)
print(root.findval(7))
# print(root.findval(2))