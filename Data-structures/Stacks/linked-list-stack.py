# IMPLEMENTING STACKS USING LINKED LISTS
from sqlalchemy import null, true


# Class to represent the stack node
class StackNode: 
    # Initialize the stack node 
    def __init__(self, data): 
        self.data = data 
        self.next = None 

# Class to represent the stack
class Stack: 
    # Create the head as a default null 
    def __init__(self): 
        self.head = null 
    
    # Checking whether the stack is empty 
    def isEmpty(self): 
        if self.head == None: 
            return True
        else: 
            return False 
    
    # Adding item to the stack 
    def addItem(self, item): 
        if self.head == None: 
            self.head = StackNode(item) # Adds item on top of the stack if there's no head
            print("% d has been pushed to stack, It is the 1st element" % (item))
        else: 
            newNode = StackNode(item)
            newNode.next = self.head 
            self.head = newNode 
            print("% d has been pushed to stack" % (item))
    
    # Remove item from the stack, we need to target the topmost element 
    def removeItem(self): 
        if self.isEmpty(): 
            return None 
        else:
            removedItem = self.head 
            self.head = self.head.next 
            removedItem.next = None 
            print("%d has been removed from the stack"% (removedItem.data))
            return removedItem.data
    
    # Checking the first item on the stack 
    def checkTop(self): 
        if self.isEmpty(): 
            return None 
        else: 
            return self.head.data

    def display(self): 
        topNode = self
        if self.isEmpty(): 
            print("Stack has no elements") 
        else: 
            while (topNode != None): 
                # print(topNode.data, '->', end='')
                print(topNode.data)
                topNode = topNode.next
                return 

# Driver code
newStack = Stack() 
print("====Adding items to the stack=======")
newStack.addItem(10)
newStack.addItem(20)
newStack.addItem(30)
newStack.addItem(40)
newStack.addItem(50)
print("======Removing the item added recently to the stack=======")
newStack.removeItem()


# Check on display() function since it doesn't work
# Check on StackNode class since it's also not working 