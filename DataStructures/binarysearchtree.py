# binarytreesearch is o of logn beacuse it uses devide and conquer
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        if self.root == None:
            return False
        temp =  self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value) # in post order we append after we go left then right
        traverse(self.root)
        return results
    
    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    
# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)        

# print(my_tree.contains(0))

# print(my_tree.min_value_node(my_tree.root).value)

my_tree_2 = BinarySearchTree()
my_tree_2.insert(47)
my_tree_2.insert(21)
my_tree_2.insert(76)
my_tree_2.insert(18)
my_tree_2.insert(27)
my_tree_2.insert(52)
my_tree_2.insert(82)

#print(my_tree_2.BFS())
#print(my_tree_2.dfs_pre_order())
#print(my_tree_2.dfs_post_order())
print(my_tree_2.dfs_in_order())