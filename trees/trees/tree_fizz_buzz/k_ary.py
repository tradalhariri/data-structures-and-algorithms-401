from trees.tree_fizz_buzz.node import Node
class KAryTree:
    
    def __init__(self,root = None):
        if root:
            self.root =  Node(root)
        else:
            self.root = root
    