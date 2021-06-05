class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextval = None

class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self, New_data):
        NewNode = Node(New_data)
        NewNode.nextval = self.head
        self.head = NewNode
    def detect(self):
        s = set()
        temp = self.head
        while (temp):
            if temp in s:
                return True
                s.add(temp)   
                temp = temp.nextval
                return False
    def Print(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.nextval
           
if __name__ == "__main__":
    ll = linkedlist()
    n = int(input("How many elements would you like to have? : "))
    for i in range(n):
        New_data = int(input("Enter data item: "))
        ll.insert(New_data)
    
    if (ll.detect()):
        print("Loop found")
    else:
        print("No loop")
    print("The linked list: ", end = ' ')
    ll.Print()
    