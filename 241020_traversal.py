class Tnode:
    def __init__(self, val):
        self.val = val
        self.left=None
        self.right=None
    def Binary_create(root):
        pass
    def pre_order(root):
        if not root:
            return
        print(root.val, end=' ')
        pre_order(root.left)
        pre_order(root.right)

    
n.val = Tnode(30)
n.left = Tnode(11)
n.left.left = Tnode(18)
n.left.right = Tnode(19)
n.left.left.left = Tnode(17)
n.right = Tnode(20)
n.right.left = Tnode(21)