# IMPLEMENTING USING QUEUE 

# Import Queue from queue library
from queue import Queue; 

# Make a new queue 
newQueue = Queue() 

# Add a new item to the newQueue using the .put() method 
newQueue.put(10)
newQueue.put(20)
newQueue.put(30)
newQueue.put(40)

# In order to access the items you have to convert the queue into a list 
print(list(newQueue.queue))

# Remove the item that was added first using the .get() method 
newQueue.get() 
print(list(newQueue.queue))
