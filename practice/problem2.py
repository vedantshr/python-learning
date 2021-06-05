class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextval= None
class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self, data):        
        if self.head is None:
            self.head = Node(data)
        currentnode = self.head
        while True:
            if currentnode.nextval is None:
                currentnode.nextval = Node(data)
                break
            currentnode = currentnode.nextval
    # def deletelist(self, removekey):
    #     Head = self.head
    #     if Head is not None:
    #         if Head.value == removekey:
    #             self.head = Head.nextval
    #             Head = None
    #             return
    #     while Head is not None:
    #         if Head.value == removekey:
    #             break
    #         prev = Head
    #         Head = Head.nextval
    #     if Head == None:
    #         return
    #     prev.nextval = Head.nextval
    #     Head = None

    def Print(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, end=' ')
            currentNode = currentNode.nextval
        print("Null")

if __name__ == "__main__":
    ll = linkedlist()
    n = int(input("How many elements would you like to have? : "))
    for i in range(n):
        data = int(input("Enter data item: "))
        ll.insert(data)
    print("The linked list: ", end = ' ')
    ll.Print()
    



        