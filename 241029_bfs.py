def BFS(root):
    q=[root]
    if not root:
        return
    while q:
        node=q.pop(0)
        print(node.value)