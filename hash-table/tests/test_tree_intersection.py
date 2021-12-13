from hash_table.tree_intersection.tree_intersection import tree_intersection,BinaryTree,Node

import pytest


def test_tree_intersection(binary_f_tree,binary_s_tree):
    assert tree_intersection(binary_f_tree,binary_s_tree)  == [100,160,125,175,200,350,500]

def test_tree_intersection_one_of_trees_is_none(binary_f_tree):
    s_binary_tree = BinaryTree()
    assert tree_intersection(binary_f_tree,s_binary_tree)  == []
    
def test_tree_intersection_no_common_values(binary_f_tree,binary_t_tree):
    assert tree_intersection(binary_f_tree,binary_t_tree)  == []

@pytest.fixture
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

@pytest.fixture
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

@pytest.fixture
def binary_t_tree():
    binary_tree = BinaryTree()
    binary_tree.root = Node(42)
    binary_tree.root.left = Node(44)
    binary_tree.root.right = Node(66)
    binary_tree.root.right.left = Node(99)

    binary_tree.root.right.right = Node(45)
    binary_tree.root.right.right.left = Node(4)
    binary_tree.root.right.right.right = Node(110)

    binary_tree.root.left.left = Node(15)
    binary_tree.root.left.right = Node(111)
    binary_tree.root.left.right.left = Node(68)
    binary_tree.root.left.right.right = Node(148)
    return binary_tree