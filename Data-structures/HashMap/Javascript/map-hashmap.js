// IMPLEMENTING HASHTABLE USING MAP OBJECT IN JAVASCRIPT 
const hashMap = new Map(); 

hashMap.set("John", "444-333-222"); 
hashMap.set("Doe", "555-666-333"); 
hashMap.set("Mary", "666-344-278");

// Get the values contained in the hashMap 
console.log(hashMap.get("John"));  // Returns 444-333-222 
console.log(hashMap.get("Steve")); // Returns undefined

// Get the size of the hashMap 
console.log(hashMap.size) // Returns 3 

