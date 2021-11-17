def print_items(n):
    '''
    Output O(n2 + n) n is insiginificant in this case and the n * n is dominant
    '''
    for i in range(n):
        for j in range(n):
            print(i, j)
            
    for k in range(n):
        print(k)