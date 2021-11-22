from collections import deque
from trees.binary_tree import BinaryTree
from trees.node import Node

def breadth_first(tree):
    if not tree.root:
        raise Exception("tree is empty")
    result = []
    queue = deque()

    queue.append(tree.root)

    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result
    
def binary_tree():
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
if __name__ == "__main__":
    print(breadth_first(binary_tree()))