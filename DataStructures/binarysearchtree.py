# binarytreesearch is o of logn beacuse it uses devide and conquer
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
my_tree = BinarySearchTree()

print(my_tree.root)
        