# Recursion is a function that calls itself until it doesent
# when the function stops calling itself and returns it is call the base case
# if a base case is not defined a stack overflow will happen

def funcThree():
    print('Three')
    
def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')
    
funcOne()