class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextval = None

class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self, New_data):
        if self.head is None:
            self.head = Node(New_data)
            return
        ND = self.head
        while True:
            if ND.nextval is None:
                ND.nextval = Node(New_data)
                break
            ND = ND.nextval                
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
    print("The linked list: ", end = ' ')
    ll.Print()
