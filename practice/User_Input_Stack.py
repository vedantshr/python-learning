class Stack:
    def __init__(self):
        self.stack = []
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def Print(self):
        if len(self.stack) <= 0:
            return print("List is empty.")
        else:
            a = 0
            for i in range(len(self.stack)):
                print(self.stack[a], end= " ")
                a = a + 1
            print("\n")
            return
if __name__ == "__main__":
    list1 = Stack()
    n = int(input("How many elements would you like to add? "))
    for i in range(n):
        dataval = int(input("Enter the data: "))
        list1.add(dataval)
    list1.Print()
