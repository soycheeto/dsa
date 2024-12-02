class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root=None
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data)
            self.in_order(node.right)

n = BinaryTree()
n.root = TreeNode(1)
n.root.left = TreeNode(2)
n.root.right = TreeNode(3)
n.root.left.left = TreeNode(4)
n.root.left.right = TreeNode(5)
n.root.right.left = TreeNode(6)
n.root.right.right = TreeNode(7)

n.in_order(n.root)



