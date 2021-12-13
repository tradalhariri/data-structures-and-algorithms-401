from hash_table.hash_table import HashTable

class Node:
    def __init__(self,value = None):
        self.left = None
        self.right = None
        self.value = value
        
class BinaryTree:
    def __init__(self,root = None):
        if root:
            self.root =  Node(root)
        else:
            self.root = None
            
def tree_intersection(f_tree,s_tree):
    if f_tree.root == None or s_tree.root == None:
        return []
    hash_table = HashTable()
    return pre_order(f_tree,s_tree,hash_table)

def pre_order(f_tree,s_tree,hash_table):
    def _travers_f_tree_pre(_root):
        hash_table.add(str(_root.value),1)
        
        if _root.left:
             _travers_f_tree_pre(_root.left)

        if _root.right:
            _travers_f_tree_pre(_root.right)
            
    _travers_f_tree_pre(f_tree.root)
    
    common = []

    def _travers_s_tree_pre(_root):
        if hash_table.contains(str(_root.value)):
            hash_table.add(str(_root.value),2)
            common.append(_root.value)
        else:
            hash_table.add(str(_root.value),1)
        
        if _root.left:
             _travers_s_tree_pre(_root.left)

        if _root.right:
            _travers_s_tree_pre(_root.right)
    _travers_s_tree_pre(s_tree.root)
    
    return common

def binary_f_tree():
    binary_tree = BinaryTree()
    binary_tree.root = Node(150)
    binary_tree.root.left = Node(100)
    binary_tree.root.right = Node(250)
    binary_tree.root.right.left = Node(200)

    binary_tree.root.right.right = Node(350)
    binary_tree.root.right.right.left = Node(300)
    binary_tree.root.right.right.right = Node(500)

    binary_tree.root.left.left = Node(75)
    binary_tree.root.left.right = Node(160)
    binary_tree.root.left.right.left = Node(125)
    binary_tree.root.left.right.right = Node(175)
    return binary_tree

def binary_s_tree():
    binary_tree = BinaryTree()
    binary_tree.root = Node(42)
    binary_tree.root.left = Node(100)
    binary_tree.root.right = Node(600)
    binary_tree.root.right.left = Node(200)

    binary_tree.root.right.right = Node(350)
    binary_tree.root.right.right.left = Node(4)
    binary_tree.root.right.right.right = Node(500)

    binary_tree.root.left.left = Node(15)
    binary_tree.root.left.right = Node(160)
    binary_tree.root.left.right.left = Node(125)
    binary_tree.root.left.right.right = Node(175)
    return binary_tree


if __name__ == "__main__":
    f_tree = binary_f_tree()
    s_tree = binary_s_tree()
    
    print(tree_intersection(f_tree, s_tree))
    
    