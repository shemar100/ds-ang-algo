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
        self.value =value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre =  self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp  = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(8)      

my_linked_list.set_value(0, 10)

help.print_list(my_linked_list)

