class Queue:
    def __init__(self):
        self.queue = list()
    def add(self, dataval):
        if dataval not in self.queue:
            self.queue.append(dataval)
            return True
        else:
            return False
    def Insert(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        else:
            return False
    def Print(self):
        a = 0
        for i in range(n):
            print(self.queue[a], end= " ")
            a = a + 1
        print("\n")
if __name__ == "__main__":
    ll = Queue()
    n = int(input("Number of elements: "))
    for i in range(n):
        dataval = int(input("Enter the data: "))
        ll.add(dataval)
    ll.Print()
    m = int(input("Number of elements to insert: "))
    for j in range(m):
        data = int(input("Enter the data: "))
        ll.Insert(data)
        n = n + 1
    ll.Print()
