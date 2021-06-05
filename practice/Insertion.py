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

ll = linkedlist()
ll.Insertion("3")
ll.Insertion("5")
ll.Insertion("7")
ll.Printlist()


