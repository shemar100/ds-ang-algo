#collision:
# to prevent collision of data within addresses we embedded the kv in another list at the address which is called separate chaining
# another method is linear probing which you search linear for a empty address 
# another way is storing kv in linked list 
# with a hashtable you increase the randomnes making iT a prime number

# hash method is O(1) 
# set item O(1)
# worst case all item at the same address which makes get O(n) best case all are in separate address whcih is O(1)

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
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.keys())

#interview question - look if list have a item common
#naive approach:
def item_in_common(list1, list2):
    # this algorithm is not efficient beacause it is O(n * n)
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(item_in_common(list1, list2))

# more efficient method
def item_in_common_2(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
    return False

#looking up a key in a hashtable is O(1) but a value is O(n)