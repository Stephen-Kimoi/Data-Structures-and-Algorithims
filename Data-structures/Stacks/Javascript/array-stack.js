// Implementing a stack data structure in js using arrays
class Stack {
    constructor(){
        this.stackItems = []; 
    } 
    
    // Adding an item to the stack
    addItem(item) {
        this.stackItems.push(item); 
        console.log(`${item} has been added to the stack!`); 
    } 

    // Removing an item from the stack
    removeItem() { 
        let topmostItem = this.stackItems[this.stackItems.length - 1];  
        this.stackItems.pop(); // It will remove the item on the top of the stack 
        console.log(`${topmostItem} has just been removed from the stack`); 
    }

    // Checking the topmost element on the stack 
    checkTopmostElement() {
        let topmostElement = this.stackItems[this.stackItems.length - 1]; 
        console.log(`The topmost element is ${topmostElement}`); 
    } 

    // Checking the size of the stack 
    checkStackSize() {
        let size = this.stackItems.length; 
        console.log(`The size of the stack is ${size}`); 
    } 

    // Clearing the stack 
    clearStack() {
        this.stackItems.length = 0; 
        console.log("The stack has just been cleared");
    }

    // CHecking if the stack is empty 
    checkIfEmpty() {
        if (this.stackItems.length === 0){
            console.log("Stack is empty"); 
        } else {
            console.log("The stack is not empty!"); 
        }
    }

} 

// Create a new instance of the stack
let stack = new Stack(); 

// Adding items into the stack
stack.addItem(10); 
stack.addItem(20); 
stack.addItem(30); 
stack.addItem(40); 

// Checking the topmost item in the stack
stack.checkTopmostElement(); 

// Checking the size of the stack
stack.checkStackSize(); 

// Removing an item from the stack
stack.removeItem(); 

// Clearing the stack 
stack.clearStack(); 

// Checking whether the stack is empty
stack.checkIfEmpty(); 