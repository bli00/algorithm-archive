import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recoverTree(root: TreeNode) -> None:
    prev = TreeNode(-sys.maxsize)
    l, r = None, None
    
    def inorder(cur: TreeNode):
        if not cur: return
        nonlocal prev, l, r    
        inorder(cur.left)
        if cur.val < prev.val:
            r = cur
            if not l: l = prev
        prev = cur
        inorder(cur.right)
        
    inorder(root)
    l.val, r.val = r.val, l.val

