import Queue

A = Queue.LinkedList()
B = Queue.LinkedList()
S = Queue.LinkedList()

A.enqueue(0)
A.enqueue(100)
A.enqueue(200)

B.enqueue(100)
B.enqueue(101)
B.enqueue(200)

while A.head is not None and B.head is not None:
    
    if(A.head.data > B.head.data):
        S.enqueue(B.head.data)
        B.head = B.head.next
    elif(B.head.data == A.head.data):
        S.enqueue(B.head.data)
        B.head = B.head.next
    
    if(B.head.data > A.head.data):
        S.enqueue(A.head.data)
        A.head = A.head.next
    elif(B.head.data == A.head.data):
        S.enqueue(A.head.data)
        A.head = A.head.next
            
if(B.head is None):
    while (A.head is not None):
        S.enqueue(A.head.data)
        A.head = A.head.next
    
if(A.head is None):
    while (B.head is not None):
        S.enqueue(B.head.data)
        B.head = B.head.next 

S.traverseQueue()
S.Size()