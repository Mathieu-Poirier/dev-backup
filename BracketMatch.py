import Stack

myStack = Stack.LinkedList()

overflow_flag = False
str = "(())"

for i in str:
    if(i not in ['[', ']', '{', '}', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']):
        print("Please enter a valid string")
        exit()
    if(i in ['[', '{', '(']):
        myStack.push(i)
    elif(i in [']', '}', ')']):
        if(myStack.head is None):
            overflow_flag = True
            print("Brackets are not balanced")
            exit()
        if(i == ']' and myStack.head.data == '[' ):
            myStack.pop()
        if(i == '}' and myStack.head.data == '{'):
            myStack.pop()
        if(i == ')' and myStack.head.data == '('):
            myStack.pop()


if(myStack.head is None and overflow_flag is False):
    print("Brackets are balanced")
if(myStack.head is not None):
    print("Brackets are not balanced")

myStack.traverseStack()
myStack.getSize()