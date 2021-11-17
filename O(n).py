# Time complexity: Time complexity is the amount of time required to execute the algorithm.
# Space complexity: Space complexity is the amount of memory required to execute the algorithm.

def print_items(n):
    '''
    ran n + n times or O(2n) but can be rewritten with constant infront of n dopped as O
    '''
    for i in range(n):
        print(i)
        
    for j in range(n):
        print(j)
        
print_items(10)