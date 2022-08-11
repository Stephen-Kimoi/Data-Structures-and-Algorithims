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

    print("The item {} has been added to the stack", item)  

 

# function for removing item from the stack  

def removeItem(stack):  

    if  (stackIsEmpty(stack)):  

      return str(-maxsize - 1)  # I don’t understand this function  
    
    print("The item added onto the stack has just been removed")
    return stack.pop()  
    

# function for checking the topmost element in the stack 

def checkStackTop(stack):  

    if (stackIsEmpty(stack)):  

        return str(-maxsize - 1) # I still have no idea what this does  

    return stack[len(stack) - 1] 

 

# Check whether the above functions work  

stack = createStack()  # create a variable named stack  

addItem(stack, str(10)) 
addItem(stack, str(20)) 
addItem(stack, str(30)) 
addItem(stack, str(40)) 

print(stack) # print the items added onto the stack 

removeItem(stack)
print(stack)