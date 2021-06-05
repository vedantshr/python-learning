# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class doubly_linked_list:
#     def __init__(self):
#         self.head = None
#     def push(self, newdata):
#         NewNode = Node(newdata)
#         NewNode.next = self.head
#         if self.head is not None:
#             self.head.prev = NewNode
#         self.head = NewNode
#     def Print(self, node):
#         while node is not None:
#             print(node.data, end=" ")
#             last = node
#             node = node.next

# dll = doubly_linked_list()
# dll.push("1")
# dll.push("2")
# dll.push("3")
# dll.Print(dll.head)

#Program Insertion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
    def push(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
    def Insert(self, prev_node, newdata):
        if prev_node is None:
            return
        NewNode = Node(newdata)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode
    def Append(self, NewVal):
        NewNode = Node(NewVal)
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


    # def Print(self, node):
    #     while node is not None:
    #         print(node.data, end=" ")
    #         last = node
    #         node = node.next
    def Print(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.data, end=" ")
            currentnode = currentnode.next
        print("Null")
if __name__ == "__main__":
    n = int(input("Enter the number of elements you would like to add: "))
    dll = doubly_linked_list()
    # dll.push("1")
    # dll.push("2")
    # dll.push("3")
    # dll.Insert(dll.head.next,"4")
    # dll.Print(dll.head)
    for i in range(n):
        newdata = int(input("Enter data: "))
        dll.push(newdata)        
    dll.Print()
    k = int(input("Enter the number of elements you would like to insert: "))
    for j in range(k):
        newdata = int(input("Enter data: "))
        dll.Insert(dll.head.next, newdata)
    dll.Print()
    m = int(input("Enter the number of elements you would like to append: "))
    for i in range(m):
        NewVal = int(input("Enter data: "))
        dll.Append(NewVal)
    dll.Print()



