class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval 
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def listprint(self):
        printval =  self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, Newdata):
        Newnode = Node(Newdata)
        if self.headval is None:
            self.headval = Newnode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = Newnode

    def InMiddle(self, middle_node, newdata1):
        if middle_node is None:
            print("The required node is absent")
            return
        Newnode1 = Node(newdata1)
        Newnode1.nextval =  middle_node.nextval
        middle_node.nextval = Newnode1

    def delete(self, removeKey):
        Headval = self.headval
        if Headval is not None:
            if Headval.dataval == removeKey:
                self.headval = Headval.nextval
                Headval = None
                return
        while Headval is not None:
            if Headval.dataval == removeKey:
                break
            prev = Headval
            Headval = Headval.nextval
        if Headval == None:
            return
        prev.nextval = Headval.nextval
        Headval = None

list1 = SLinkedList() 
list1.headval = Node("Mon") 
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node 
list1.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3
list1.AtBeginning("Sun")
# list1.InMiddle(list1.headval.nextval,"Thu")
list1.InMiddle(e2.nextval,"Thu")
list1.AtEnd("Fri")
list1.delete("Fri")

list1.listprint()
