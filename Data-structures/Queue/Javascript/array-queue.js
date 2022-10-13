// IMPLEMENTING QUEUES IN JAVASCRIPT USING ARRAYS 

class Queue {
    constructor() {
        this.data = []
    }

    // Enqueue method for adding elements into the queue 
    enqueue(item) {
        this.data.push(item);
        console.log(`${item} as just been added to the queue`); 
    }  

    // dequeue method for removing elements from the queue 
    dequeue() {
        if (this.data.length === 0){
            console.log("The queue is already empty")
        } else {
            let removedItem = this.data[0]; 
            this.data.pop(); 
            console.log(`${removedItem} has just been removed from the queue`); 
        }
    }

    // Method to check whether the queue is empty 
    isEmpty() {
        if (this.data.length === 0){
            console.log("The queue is empty"); 
        } else {
            console.log("The queue is not empty"); 
        }
    } 

    // Method to check the topmost element
    checkTop() {
        if (this.data.length === 0){
            console.log("Nothing here to see, the queue is empty!"); 
        } else {
            let topElement = this.data[0]; 
            console.log(`The topmost element is ${topElement}`); 
        }
    }

    // Function for printing the queue
    printQueue() {
        let queue = ""; 
        this.data.forEach( item => {
            queue += item + " "; 
        })
        console.log(queue); 
    } 


} 

let queue = new Queue(); 

// Adding items to the queue 
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

// Checking the topmost element 
queue.checkTop(); 

// Removing item from the queue 
queue.dequeue(); 

// Print all the items in thq queue 
queue.printQueue(); 

