# METHOD 2 OF IMPLEMENTING HASHMAPS
# This is a longer method, I derived it from https://sothunt.net  


from secretstorage import Item


class HashTable: 
    # Create an empty bucket list 
    def __init__(self, size):
        self.size = size 
        self.hash_table = [[]]
    
    
    # Function for inserting values 
    def insert_value(self,key,val): 
        # Get index from the key using hash functions 
        hashed_key = hash(key) % self.size 

        # Get bucket corresponding to the index 
        bucket = self.hash_table[hashed_key] 

        found_key = False 
        for index, record in enumerate(bucket): 
            record_key, record_val = record
            # Check if the bucket has the same key as the key to be inserted
            if record_key == key: 
                found_key = True 
                break

        if found_key: 
            bucket[index] = (key, val) 
        else: 
            bucket.append((key,val))


    # Return searched val with specific key 
    def get_val(self, key): 
        # Get index from the key using hash function 
        hashed_key = hash(key) % self.size 

        # Get the bucket corresponding to the index 
        bucket = self.hash_table[hashed_key]
        
        found_key = False 
        for index, record in enumerate(bucket): 
            record_key, record_val = record 

            # Check if the bucket has the same key as the key being searched 
            if record_key == key: 
                found_key = True
                break 

        # If the bucket has the same key as the key being searched return the value being found 
        if found_key: 
           return record_val
        else: 
            return "No record found"
        
    # Remove tha value with a specific key 
    def delete_val(self, key): 
        # Get index from the key using the hash function 
        hashed_key = hash(key) % self.size 

        # Get the bucket corresponding to the index 
        bucket = self.hash_table[hashed_key]
        found_key = False 
        for index, record in enumerate(bucket): 
            record_key, record_value = record
            # Check if the bucket has the same key as the key to be deleted 
            if record_key == key: 
                found_key = True 
                break
        if found_key: 
            bucket.pop(index)
        return 
    
    # To print the items of the hashmap 
    def __str__(self): 
        return "".join(
            str(item) for item in self.hash_table
        )


# Create a hashtable 
newHashTable = HashTable(1)

# Insert some values 
newHashTable.insert_value("key1","value1")
print(newHashTable)
print("---")

newHashTable.insert_value("key2","value2")
print(newHashTable)
print("---")

# Search or access values 
print(newHashTable.get_val("key1")) 
print("---") 

# Delete value from the hashtable 
newHashTable.delete_val("key2")
print("Key 2 deleted from the hashtable") 
print(newHashTable)
               