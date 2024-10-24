class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right=None

def preorder(node):
    if node is None:
        return
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=' ')

n = Node('Dubai')
n.left = Node('Deira')
n.left.left = Node('Muraqqabat')
n.left.right = Node('Muteena')
n.right = Node('Bur Dubai')
n.right.left = Node('Oud Metha')
n.right.right = Node('Raffa')

preorder(n)
inorder(n)
postorder(n)