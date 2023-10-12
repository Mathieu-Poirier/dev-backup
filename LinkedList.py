class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def addFirst(self, data):
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
    
    def addLast(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.size = self.size + 1
            return self.head

        current_node = self.head

        while(current_node != None):
            if(current_node.next == None):
                current_node.next = new_node
                self.size = self.size + 1
                return
            current_node = current_node.next
        return   
    
    def removeFirst(self):
        temp = Node(None)
        if self.head is None:
            print("List is empty, cannot remove a node")
        else:
            temp = self.head
            self.head = self.head.next
            self.size = self.size - 1
            del temp
    
    def removeLast(self):
        temp = Node(None)
        current_node = self.head
        
        if self.head is None:
            print("List is empty, cannot remove a node")
            return self.head
        if self.head.next is None:
            self.head = None
            self.size = self.size - 1
            return self.head
        else:
            while(current_node != None):
                if(current_node.next.next == None):
                    temp = current_node.next
                    current_node.next = None
                    self.size = self.size - 1
                    del temp
                    return current_node.data
                current_node = current_node.next

    def getLast(self):
        current_node = myList.head


        while (current_node != None):
            if(current_node.next == None):
                print(">> ",current_node.data)
                return
            current_node = current_node.next
           

    def getFirst(self):
        print("\n>> ", self.head.data)

    def getSize(self):
        print(" Size: ", self.size)

    def traverseList(self):
        curr_node = self.head
        while (curr_node != None):
            print(f"{curr_node.data} >> ", end="")
            curr_node = curr_node.next
        print(f"{curr_node}", end="")


    
"""
myList = LinkedList()

myList.addFirst(2)
myList.addFirst(1)
myList.traverseList()
myList.getFirst()
myList.getLast()
myList.addFirst(85)
myList.addFirst(222)
myList.addLast(444)
myList.addLast(666)
myList.addFirst(888)
myList.traverseList()
myList.getSize()
myList.removeFirst()
myList.removeLast()
myList.traverseList()
myList.getSize()
"""

