def print_items(n):
    '''
    ran n * n times or (n^2) 
    '''
    for i in range(n):
        for j in range(n):
            print(i, j)
            
print_items(10)