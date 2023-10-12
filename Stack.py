class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size = self.size + 1
            return self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.size = self.size + 1
            return self.head
    
    def pop(self):
        temp = Node(None)
        if self.head is None:
            print("List is empty, cannot remove a node")
        else:
            temp = self.head
            self.head = self.head.next
            self.size = self.size - 1
            del temp          

    def getFirst(self):
        print("\n>> ", self.head.data)

    def getSize(self):
        print(" Size: ", self.size)

    def traverseStack(self):
        curr_node = self.head
        while (curr_node != None):
            print(f"{curr_node.data} >> ", end="")
            curr_node = curr_node.next
        print(f"{curr_node}", end="")



"""
Stack = LinkedList()

Stack.push(1)
Stack.push(2)
Stack.push(3)
Stack.push(4)
Stack.pop()
Stack.pop()
Stack.pop()
Stack.pop()
Stack.traverseStack()
"""
