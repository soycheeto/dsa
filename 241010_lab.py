class TreeNode:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_pre_order_recursive(node):
    if node:
        print(node.value, end=' ')
        dfs_pre_order_recursive(node.left)
        dfs_pre_order_recursive(node.right)

def dfs_pre_order_iterative(root):
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.value, end=' ')
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.right = TreeNode('F')

print("DFS Pre-Order Traversal (Recursive):")
dfs_pre_order_recursive(root)
print()

print("DFS Pre-Order Traversal (Iterative):")
dfs_pre_order_iterative(root)
print()