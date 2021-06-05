class Stack:
    def __init__(self):
        self.stack = []
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
    def remove(self):
        if len(self.stack) <= 0:
            print("List is empty.")
        else:
            return self.stack.pop()
    def Print(self):
        a = 0
        for i in range(len(self.stack)):
            print(self.stack[a], end=" ")
            a = a + 1
        print("\n")
if __name__ == "__main__":
    list1 = Stack()
    list1.add("Mon")
    list1.add("Tue")
    list1.add("Wed")
    list1.add("Thu")
    print(list1.peek())
    list1.Print()
    list1.remove()
    list1.Print()
        
    
    

