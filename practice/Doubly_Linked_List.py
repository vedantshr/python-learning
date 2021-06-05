class Node:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data
class doublylinkedlist:
    def __init__(self):
        self.head = None
    def Insert(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head.prev = NewNode
        self.head = NewNode
    # def Append(self, newdata):
    #     NewNode = Node(newdata)
    #     NewNode.next = None
    #     if self.head is None:
    #         NewNode.prev = None
    #         self.head = NewNode
    #         return
    #     last = self.head
    #     while (last.next is not None):
    #         last = last.next
    #     last.next = NewNode
    #     NewNode.prev = last
    #     return
    def Append(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return
    def Push(self, prev_node, newdata):
        if prev_node is None:
            return
        NewNode = Node(newdata)
        NewNode.next = prev_node.next #This is the step where we are mentioning that next node of previous node is now the next node of newnode.
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode 
    def Print(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.data, end=" ")
            currentnode= currentnode.next
        print("Null")
if __name__ == "__main__":
    dll = doublylinkedlist()
    n = int(input("Number of elements: "))
    for i in range(n):
        newdata = int(input("Enter data: "))
        dll.Insert(newdata)
    dll.Print()
    m = int(input("Number of elements: "))
    for i in range(m):
        newdata = int(input("Enter data: "))
        dll.Append(newdata)
    dll.Print()
    a = int(input("after how many digits would you like to add: "))
    b = dll.head
    for i in range(a):
        b = b.next       
    dll.Push(b, "20")
    dll.Print()


