# IMPLEMENTING QUEUES USING ARRAYS 

class Queue: 
    # Initialize the object 
    def __init__(self, c): 
        self.queue = [] 
        self.front = self.rear = 0 
        self.capacity = c 

    # Insert an element at the end(rear) of the queue (Enqueue)
    def insertElement(self, data): 
        # Check whether the queue is full
        if (self.capacity == self.rear): 
            print("\nQueue is full") 
        else: 
            self.queue.append(data) 
            self.rear += 1 

    # Function to delete an element from the front of the queue (Dequeue) 
    def deleteElement(self): 
        # Check whether the queue is empty 
        if (self.front == self.rear): 
            print("Queue is empty") 
        else: 
            x = self.queue.pop(0) 
            self.rear -= 1 

    # Display the queue elements 
    def displayQueue(self):
        if(self.rear == self.front): 
            print("\nQueue is empty") 
        else: 
            for i in self.queue: 
                print(i,'<-',end="")

    # Print the first element in the queue (front)
    def displayFront(self): 
        if (self.front == self.rear):
            print("\nQueue is empty") 
        
        print("\nFront element is: ", 
          self.queue[self.front])

# Driver code 
if __name__ == '__main__': 
    print("Queue in python")
    #  Make a new queue of capacity 5 
    newQueue = Queue(5) 

    # Display the queue elements 
    newQueue.displayQueue() 

    # Insert elements into the queue 
    newQueue.insertElement(10)
    newQueue.insertElement(20)
    newQueue.insertElement(30)
    newQueue.insertElement(40)
    newQueue.insertElement(50) 

    # Display the inserted elements 
    newQueue.displayQueue() 

