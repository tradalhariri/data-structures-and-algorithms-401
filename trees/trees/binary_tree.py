from trees.node import Node
from collections import deque
 
class BinaryTree:

    def __init__(self,root = None):
        if root is not None:
            self.root =  Node(root)
        else:
            self.root = None

    def pre_order(self):
        if self.root is None:
            raise Exception("tree is empty")
        tree_output = []
        def _travers_pre(_root):
            tree_output.append(_root.value)

            if _root.left:
                _travers_pre(_root.left)

            if _root.right:
                _travers_pre(_root.right)
            return tree_output

        return _travers_pre(self.root)

    def in_order(self):
        if self.root is None:
            raise Exception("tree is empty")
        tree_output = []
        def _travers_in(_root):
            

            if _root.left:
                _travers_in(_root.left)
            tree_output.append(_root.value)

            if _root.right:
                _travers_in(_root.right)
            return tree_output

        return _travers_in(self.root)

    def post_order(self):
        if self.root is None:
            raise Exception("tree is empty")
        tree_output = []
        def _travers_post(_root):
            

            if _root.left:
                _travers_post(_root.left)
            

            if _root.right:
                _travers_post(_root.right)
            
            tree_output.append(_root.value)
            return tree_output

        return _travers_post(self.root)

    def max_value(self):
        stack = deque()
        stack.append(self.root)
        max_value  = self.root.value

        while stack:
            current = stack.pop()
            if current.value > max_value:
                max_value = current.value
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return max_value
            
        
def binary_tree_2():
    binary_tree = BinaryTree()
    binary_tree.root = Node(2)
    binary_tree.root.left = Node(7)
    binary_tree.root.right = Node(5)
    binary_tree.root.right.right = Node(9)
    binary_tree.root.right.right.left = Node(4)
    binary_tree.root.left.left = Node(2)
    binary_tree.root.left.right = Node(6)
    binary_tree.root.left.right.left = Node(5)
    binary_tree.root.left.right.right = Node(11)
    return binary_tree

def create_tree():
    tree=BinaryTree("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    return tree

if __name__ == "__main__":
    tree = create_tree()
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())
    tree_2 = binary_tree_2()
    print(tree_2.max_value())
    # travers_pre = tree.pre_order()
    # print(travers_pre(tree.root)) 