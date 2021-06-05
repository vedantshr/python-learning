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
    def Printlist(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.nextval
        print("Null")
    def deletelist(self, removekey):
        Head = self.head
        if Head is not None:
            if Head.value == removekey:
                self.head = Head.nextval
                Head = None
                return
        while Head is not None:
            if Head.value == removekey:
                break
            prev = Head
            Head = Head.nextval
        if Head == None:
            return
        prev.nextval = Head.nextval
        Head = None

ll = linkedlist()
# ll.Insertion("3")
# ll.Insertion("5")
# ll.Insertion("7")
ll.head = Node("3")
e2 = Node("5")
e3 = Node("7")
e4 = Node("9")
ll.head.nextval = e2
e2.nextval = e3
e3.nextval = e4
ll.Printlist()
ll.deletelist("9")
ll.Printlist()



