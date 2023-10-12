class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size = self.size + 1
            return self.head

        self.tail.next = new_node
        self.tail = new_node
        self.size = self.size + 1
         
    
    def dequeue(self):
        temp = Node(None)
        if self.head is None:
            print("List is empty, cannot remove a node")
        else:
            temp = self.head
            self.head = self.head.next
            self.size = self.size - 1
            del temp

    def getLast(self):
        current_node = myList.head


        while (current_node != None):
            if(current_node.next == None):
                print(">> ",current_node.data)
                return
            current_node = current_node.next
           

    def front(self):
        print("Front node:", self.head.data)

    def Size(self):
        print(" Size: ", self.size)
    
    def isEmpty(self):
        if(self.head is None):
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def traverseQueue(self):
        curr_node = self.head
        while (curr_node != None):
            print(f"{curr_node.data} >> ", end="")
            curr_node = curr_node.next
        print(f"{curr_node}", end="")
"""
Queue = LinkedList()

Queue.enqueue(10)
Queue.enqueue(20)
Queue.dequeue()
Queue.dequeue()
Queue.enqueue(30)
Queue.enqueue(40)
Queue.enqueue(50)
Queue.dequeue()
Queue.dequeue()
Queue.dequeue()
Queue.isEmpty()
Queue.enqueue(50)
Queue.enqueue(50)
Queue.enqueue(45)
Queue.isEmpty()
Queue.front()

Queue.traverseQueue()
Queue.Size()
"""