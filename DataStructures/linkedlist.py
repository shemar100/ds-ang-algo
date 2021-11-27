# Linked list Big(O) - 
# append: O(1)
    # a node to the end of a linked list we have to have the last node pointed to it
    # Then tail pointed to it and then it's added to the lis which is O(1)

# remove: O(n)
    # Have tail pointed to node before
    # removeing from the end is more compicated, in other to have tail point to node
    # we have to iterate from the head to reach the last node then we can set pointer equal to the last node
    # Becaue we had to iterate through the entire list it is O(n)
    
#preprend: O(1)
    # it just reassign the node to head and it does matter how man item in the list
    # which makes it O(1)
    
# remove item from head of linkedlist: O(1)
    # reassigns head to nextnode
    # the operation happens at constant time beacuse it doesnt matter how many item is in the list
    
# adding item to middle of linkedlist: O(n)
    # we have to iterate to find the middle which is O(n)
    # then have the new node pointted to the previous node whcih happens at constant time
    
# removing from the middle of list list: O(n)
    # assuming we still might have to go through the list
    # then remove the node which happens at constant time
    
# lookup linkedlist: O(n)
    # beacause a linkedlist doesnt carries index much like list we have to iterate through the list 
#create a class for creating a node
import helper as help

class Node:
    def __init__(self, value):
        self.value =value   #value of the node
        self.next = None   #next node

class LinkedList:
    def __init__(self, value):
        new_node = Node(value) # create a new node
        self.head = new_node # set the head to the new node
        self.tail = new_node # set the tail to the new node
        self.length = 1 # set the length to 1
        
    def append(self, value):
        new_node = Node(value) # create a new node
        if self.head is None: # if the list is empty
            self.head = new_node    # set the head to the new node
        else: # if the list is not empty   
            self.tail.next = new_node    # set the next node of the tail to the new node
            self.tail = new_node    # set the tail to the new node
        
        self.length += 1 # increase the length of the list
        return True # return true
    
    def pop(self):
        if self.length == 0:    # if the list is empty  
            return None     # return none
        temp = self.head   # set temp to the head
        pre =  self.head  # set pre to the head
        while(temp.next): # while the next node is not empty
            pre = temp # set pre to temp
            temp = temp.next # set temp to the next node
        self.tail = pre # set the tail to the previous node
        self.tail.next = None # set the next node of the tail to none
        self.length -= 1 # decrease the length of the list
        if self.length == 0: # if the length is 0
            self.head = None # set the head to none
            self.tail = None # set the tail to none
        return temp.value # return the value of the node
    
    def prepend(self, value): 
        new_node = Node(value)  # create a new node
        if self.length == 0: # if the list is empty
            self.head = new_node # set the head to the new node
            self.tail = new_node    # set the tail to the new node
        else: # if the list is not empty
            new_node.next = self.head # set the next node of the new node to the head
            self.head = new_node # set the head to the new node
        self.length += 1 # increase the length of the list
        return True # return true
    
    def pop_first(self):  
        if self.length == 0:    # if the list is empty
            return None    # return none
        else: # if the list is not empty
            temp  = self.head # set temp to the head
            self.head = self.head.next # set the head to the next node
            temp.next = None # set the next node of the temp to none
            self.length -= 1 # decrease the length of the list
        if self.length == 0: # if the length is 0
            self.tail = None # set the tail to none
        return temp.value # return the value of the node
    
    def get(self, index): 
        if index < 0 or index >= self.length: # if the index is less than 0 or greater than or equal to the length
            return None # return none
        temp = self.head # set temp to the head
        for _ in range(index): # for loop to iterate through the list
            temp = temp.next # set temp to the next node
        return temp # return the node
    
    def set_value(self, index, value):
        temp = self.get(index) # set temp to the node
        if temp: # if the node is not none
            temp.value = value # set the value of the node to the value
            return True # return true
        return False # return false
    
    def insert(self, index, value):
        if index < 0 or index > self.length: # if the index is less than 0 or greater than or equal to the length
            return None # return none
        if index == 0: # if the index is 0
            return self.prepend(value) # O(1)
        if index == self.length: # if the index is the length
            return self.append(value) # O(1)
        new_node = Node(value) # create a new node
        temp = self.get(index - 1) # set temp to the node
        new_node.next = temp.next # set the next node of the new node to the next node of the temp
        temp.next = new_node # set the next node of the temp to the new node
        self.length += 1   # increase the length of the list
        return True # return true
    
    # remove item from linkedlist
    def remove(self, index): 
        if index < 0 or index >= self.length: # if the index is less than 0 or greater than or equal to the length
            return None # return none
        if index == 0: # if the index is 0
            return self.pop_first() # O(1)
        if index == self.length - 1: # if the index is the length
            return self.pop()  # O(n)
        prev = self.get(index - 1)     # get the node before the node we want to remove
        temp = prev.next # set temp to the next node of the node we want to remove
        prev.next = temp.next    # set the next node of the previous node to the next node of the next node
        temp.next = None # set the next node of the temp to none
        self.length -= 1 # decrease the length of the list
        return temp.value # return the value of the node
    
    def reverse(self): 
        temp = self.head # set temp to the head
        self.head = self.tail # set the head to the tail
        self.tail = temp # set the tail to the temp
        after = temp.next # set after to the next node of the temp
        before = None # set before to none
        for _ in range(self.length):
            after = temp.next # set after to the next node of the temp
            temp.next = before # set the next node of the temp to before
            before = temp # set before to the temp
            temp = after # set temp to the after

    
    
            
    
my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(8)      

my_linked_list.set_value(0, 10)

help.print_list(my_linked_list)

print(my_linked_list.remove(0), '\n')
my_linked_list.reverse()
help.print_list(my_linked_list)

