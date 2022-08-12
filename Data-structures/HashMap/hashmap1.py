# METHOD 1 OF IMPLEMENTING HASHMAPS IN PYTHON 

# Creating a dictionary and adding entries into it
newHashMap = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}
print("New hashmap created \n", newHashMap)

# Adding a new entry
newHashMap['key5'] = 'value5'
print("New entry 5 added into the hashmap \n", newHashMap)

# Deleting an entry 
del newHashMap['key1']
print("Value 1 deleted from the entry \n", newHashMap) 