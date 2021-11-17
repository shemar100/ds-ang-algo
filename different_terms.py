# Logoritmic runtime.
# Different term input

def print_items(a, b):
    '''
    first for loop is O(a) and second for loop is O(b) when addes together is O(a+b)
    '''
    for i in range(a):
        print(a)
        
    for i in range(b):
        print(b)
        
def print_items_2(a, b):
    '''
    As a nested loop it would be O(a*b)
    '''
    for i in range(a):
        print(a)
        for i in range(b):
            print(b)
        