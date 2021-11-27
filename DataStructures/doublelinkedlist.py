import helper as help

class Node:
    # Node constriuctor for Doubly Linked List
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    # append a node to the end of the list
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    # pop a node from the doubly linked list
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.tail.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)  # create a new node
        if self.length == 0: # if the list is empty
            self.head = new_node # set the head to the new node
            self.tail = new_node    # set the tail to the new node
        else: # if the list is not empty
            new_node.next = self.head # set the next node of the new node to the head   
            self.head.prev = new_node # set the prev node of the head to the new node
            self.head = new_node # set the head to the new node
        self.length += 1 # increase the length of the list
        return True # return true
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False    
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
    
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next  
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
my_double_linked_list = DoublyLinkedList(2)
my_double_linked_list.append(3)
my_double_linked_list.prepend(1)

print(my_double_linked_list.get(0).value)
print(my_double_linked_list.get(1).value)
