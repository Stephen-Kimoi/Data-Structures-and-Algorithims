// IMPLEMENTING HASH TABLES / HASH MAPS IN JAVASCRIPT 

class HashTable {
    constructor() {
        this.hashTableValues = new Array(107); 
        this.hashTableSize = 0; 
    } 

    // Create a private method that transoforms the key into index
    _createHash(key) { 
        let hash = 0; 
        for (let i = 0; i < key.length; i++){
            hash += key.charCodeAt(i); 
        }
        let finalHash = hash % this.hashTableValues.length; 
        return finalHash
    }
    
    // Set function for inserting values into the hashtable
    set(key, value) {
        const index = this._createHash(key); 
        this.hashTableValues[index] = [key, value]; 
        this.hashTableSize++
    }

    // Get function for getting values from the hashtable
    get(key) {
        const index = this._createHash(key); 
        const value = this.hashTableValues[index]; 
        if (value === undefined){
            console.log(`The item "${key}" does not exist`)
        } else {
            console.log(value); 
        }
    }

    // Remove function that deletes values from the hashtable
    remove(key) {
       const index = this._createHash(key); 

       if(this.hashTableValues[index]){
           console.log(`Item ${this.hashTableValues[index]} has been successfully removed!`)
           this.hashTableValues[index] = undefined; 
           this.hashTableSize--; 
       } else {
           console.log("Item not found"); 
       }
    }
}

// Create a new instance of the hashtable
const hashTable = new HashTable(); 

// Add values to the hashtable
hashTable.set("America",001); 
hashTable.set("Africa",003); 
hashTable.set("Asia",004); 
hashTable.set("Europe",005); 

// Try to retrieve an item that isn't available in the hashtable - this will log "The item does not exist"
hashTable.get("Steve");

// Retrieve an item in the hashtable 
hashTable.get("Asia");

// Log the hashtable and its size
console.log("\n Hashtable size: ", hashTable.hashTableSize); 
console.log("\n Hashtable items: ", hashTable.hashTableValues); 