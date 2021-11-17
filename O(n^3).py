def print_items(n):
    '''
    ran n * n * n times or (n^3) 
    '''
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
            
print_items(10)