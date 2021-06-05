# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.nextval = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def printnode(self):
#         currentNode = node1
#         while True:
#             print (currentNode.head, "->"),
#             if currentNode.nextval is None:
#                 print("Null")
#                 break
#             currentNode = currentNode.nextval

# node1 = LinkedList()
# node1.head = Node("3")
# node2 = Node("5")
# node3 = Node("7")

# node1.head.nextval = node2
# node2.nextval = node3
# node1.printnode()

class linkedlistnode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

node1 = linkedlistnode("3")
node2 = linkedlistnode("5")
node3 = linkedlistnode("7")

node1.nextNode = node2
node2.nextNode = node3

currentNode = node1
while True:
    print (currentNode.value),
    if currentNode.nextNode is None:
        print("Null")
        break
    currentNode = currentNode.nextNode



