from trees.binary_tree import BinaryTree
from trees.node import Node

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self,value):
        if  self.root is None:
            self.root = Node(value)
            return
        temp = self.root
        correct_location = False
        while not correct_location:
            if value < temp.value:
                if not temp.left:
                    temp.left = Node(value)
                    correct_location = True
                    continue
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = Node(value)
                    correct_location = True
                    continue
                temp = temp.right

    def contains(self,value):
        def _search(_root):
            if _root is None:
                return False
            if _root.value == value :
                return True
            if value < _root.value:
                return _search(_root.left)
            else:
               return _search(_root.right)
        return _search(self.root)

if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()

    binary_search_tree.add(100)

    binary_search_tree.add(20)
    binary_search_tree.add(500)
    binary_search_tree.add(10)
    binary_search_tree.add(30)
    binary_search_tree.add(40)
    binary_search_tree.add(600)
    print(binary_search_tree.pre_order())
    print(binary_search_tree.contains(100))
    print(binary_search_tree.contains(20))
    print(binary_search_tree.contains(10))
    print(binary_search_tree.contains(30))
    print(binary_search_tree.contains(40))
    print(binary_search_tree.contains(500))
    print(binary_search_tree.contains(600))
    print(binary_search_tree.contains(548))
    print(binary_search_tree.contains(55))

