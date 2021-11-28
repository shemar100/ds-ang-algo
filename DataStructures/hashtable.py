#collision:
# to prevent collision of data within addresses we embedded the kv in another list at the address which is called separate chaining
# another method is linear probing which you search linear for a empty address 
# another way is storing kv in linked list 
# with a hashtable you increase the randomnes making iT a prime number

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
        
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) #ord stands fpr odorinal leeter which gets the ascii value for eachletter
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]  is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.get_item('bolts'))