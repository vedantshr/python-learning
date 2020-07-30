class library:
    def __init__(self, name, listOfBooks):
        self.nameOflibrary = name
        self.listOfBooks = listOfBooks

    def findNoOfBooks(self):
        return len(self.listOfBooks)

    def addBook(self, bookname, bookquantity):
        self.listOfBooks.append([bookname, bookquantity])

if __name__ == "__main__":
    obj = library("ABC Library", [["A", 12], ["B",10], ["c", 5]])
    print (obj.findNoOfBooks())
    obj.addBook("Let us C", 1)
    print (obj.listOfBooks)

    obj2 = library("XYZ Library", ["x",2])
    obj2.addBook("python", 2)
    print (obj2.listOfBooks)