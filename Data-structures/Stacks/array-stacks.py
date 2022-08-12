# IMPLEMENTING STACKS USING ARRAYS IN PYTHON

# Import maxsize from sys module: it checks the larges value a variable of a data type can store  
from sys import maxsize  

#function for creating stack 
def createStack():    
    stack = []    # create an empty array and name it stack  
    return stack    

# function for checking whether the stack is empty 
def stackIsEmpty(stack):  
    return len(stack) == 0  # returns a boolean value of true since the length of the stack is 0  

 

# function for adding an item to the stack  

def addItem(stack, item):  
    stack.append(item)  # append() function adds an item into the array 
    print( item + " has been added to the stack")  
    print(stack)

 

# function for removing item from the stack  

def removeItem(stack):  
    if  (stackIsEmpty(stack)):  
      return str(-maxsize - 1)  
    print("Item " + stack[len(stack) - 1] + " has just been removed")
    return stack.pop()  
    

# function for checking the topmost element in the stack 

def checkStackTop(stack):  
    if (stackIsEmpty(stack)):  
        return str(-maxsize - 1)   
    print("The element on top of the stack is:", stack[len(stack) - 1]) 

 

# Check whether the above functions work  

stack = createStack()  # create a variable named stack  

# Add items to the stack
addItem(stack, str(10)) 
addItem(stack, str(20)) 
addItem(stack, str(30)) 
addItem(stack, str(40)) 

#Remove items from the stack
removeItem(stack)
print("Elements present in the stack", stack)

#Check the topmost element in the stack
checkStackTop(stack)