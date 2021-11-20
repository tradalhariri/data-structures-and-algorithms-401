from trees import __version__
from trees.binary_tree import BinaryTree
from trees.binary_search_tree import BinarySearchTree
from trees.node import Node

import pytest

def test_version():
    assert __version__ == '0.1.0'

# Can successfully instantiate an empty tree

def test_instantiate_empty_binary_tree():
    binary_tree = BinaryTree()
    assert binary_tree.root == None

def test_instantiate_empty_binary_search_tree():
    binary_search_tree = BinarySearchTree()
    assert binary_search_tree.root == None  

# Can successfully instantiate a tree with a single root node

def test_instantiate_binary_tree_single_root():
    binary_tree = BinaryTree("A")
    assert binary_tree.root.value == "A"

def test_instantiate_binary_search_tree_single_root():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.root = Node(5)
    assert binary_search_tree.root.value == 5

# Can successfully add a left child and right child to a single root node
def test_binary_tree_add_left_and_right_childs_to_single_root():
    binary_tree = BinaryTree("A")
    binary_tree.root.left = Node("B")
    binary_tree.root.right = Node("C")
    assert binary_tree.root.left.value == "B"
    assert binary_tree.root.right.value == "C"

def test_binary_search_tree_add_left_and_right_childs_to_single_root():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(5)
    binary_search_tree.add(3)
    binary_search_tree.add(10)

    assert binary_search_tree.root.value == 5
    assert binary_search_tree.root.right.value == 10
    assert binary_search_tree.root.left.value == 3
# Can successfully return a collection from a preorder traversal

def test_return_collection_pre_order_binary_tree(binary_tree):
    assert ["A","B","D","E","C","F"] == binary_tree.pre_order()
# Can successfully return a collection from an inorder traversal

def test_return_collection_in_order_binary_tree(binary_tree):
    assert ["D","B","E","A","F","C"] == binary_tree.in_order()
# Can successfully return a collection from a postorder traversal

def test_return_collection_post_order_binary_tree(binary_tree):
    assert ["D","E","B","F","C","A"] == binary_tree.post_order()


# Can successfully return a collection from a preorder traversal

def test_return_collection_pre_order_binary_search_tree(binary_search_tree):
    assert [100,20,10,30,40,500,600] == binary_search_tree.pre_order()
# Can successfully return a collection from an inorder traversal

def test_return_collection_in_order_binary_search_tree(binary_search_tree):
    assert [10,20,30,40,100,500,600] == binary_search_tree.in_order()
# Can successfully return a collection from a postorder traversal

def test_return_collection_post_order_binary_search_tree(binary_search_tree):
    assert [10,40,30,20,600,500,100] == binary_search_tree.post_order()

def test_binary_search_tree_contains(binary_search_tree):
    assert binary_search_tree.contains(5) == False
    assert binary_search_tree.contains(10) == True

def test_pre_order_binary_tree_raise_exception_when_tree_is_empty():
    binary_tree = BinaryTree()
    with pytest.raises(Exception):
        binary_tree.pre_order()
        
  
@pytest.fixture
def binary_tree():
    binary_tree = BinaryTree("A")
    binary_tree.root.left=Node("B")
    binary_tree.root.right=Node("C")
    binary_tree.root.left.left=Node("D")
    binary_tree.root.left.right=Node("E")
    binary_tree.root.right.left=Node("F")
    return binary_tree

@pytest.fixture
def binary_search_tree():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(100)
    binary_search_tree.add(20)
    binary_search_tree.add(500)
    binary_search_tree.add(10)
    binary_search_tree.add(30)
    binary_search_tree.add(40)
    binary_search_tree.add(600)

    return binary_search_tree