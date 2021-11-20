from trees.node import Node
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
    # travers_pre = tree.pre_order()
    # print(travers_pre(tree.root)) 