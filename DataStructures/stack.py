class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    # Stack is LIFO: Last in first out
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        
    def pop(self):
        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    

        
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
            

new_stack = Stack(1)
new_stack.push(2)
new_stack.push(4)

new_stack.print_stack()

print(new_stack.pop())