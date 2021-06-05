class Node:
    def __init__(self, value, nextval=None):
        self.value = value
        self.nextval = nextval
class linkedlist:
    def __init__(self, head=None):
        self.head = head
    def Insertion(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextval is None:
                currentNode.nextval = node
                break
            currentNode = currentNode.nextval
    def MiddleInsertion(self, middle_val, newData):
        if middle_val is None:
            print("The required node is absent.")
            return
        NewData = Node(newData)
        NewData.nextval = middle_val.nextval
        middle_val.nextval = NewData


    def Printlist(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.nextval
        print("Null")

ll = linkedlist()
# ll.Insertion("3")
# ll.Insertion("5")
# ll.Insertion("7")
# ll.Printlist()
ll.head = Node("3")
e2 = Node("5")
e3 = Node("7")
e4 = Node("9")
ll.head.nextval = e2
e2.nextval = e3
e3.nextval = e4
ll.MiddleInsertion(ll.head,"2")
ll.Printlist()



