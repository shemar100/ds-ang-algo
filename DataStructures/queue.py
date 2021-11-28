class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    # queue is first in first out
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.lenth = 1
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.lenth += 1
        
        
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
my_queue = Queue(1)        
my_queue.enqueue(2)
        
my_queue.print_queue()