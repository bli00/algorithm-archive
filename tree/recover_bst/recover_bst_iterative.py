import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recoverTree(root: TreeNode) -> None:
    # 'prev' is the node left of 'cur' in a sorted array of the BST nodes.
    # 'prev' is initialized as a bookmarker.
    prev = TreeNode(-sys.maxsize) 
    # 'l' is the first node that appears out of place.
    # 'r' is the consecutive node to the right of 'l' in the sorted
    # array. 'r' exists to handle edge cases when two consecutive
    # nodes are swapped.
    l, r = None, None
   
    # iterative inorder traversal to read nodes from left to right
    # in an sorted fashion. Since it's a BST, an inorder traversal should
    # reveal a monotonically increasing pattern. When a decrease is detected,
    # something has been misplaced. 
    stack = []
    while stack or root:
        if root:
            # greedily add all left elements to the stack
            stack.append(root)
            root = root.left
        else:
            # pop an element from the stack whenever our 'root' pointer
            # is None. In which case 'cur' is the next element in our sorted
            # list.
            cur = stack.pop()
            if cur.val < prev.val:
                # if there is a decrease, something is out of place.
                if l:
                    # if the previous out of place node has been initiated,
                    # the 'cur' l node must be swapped with previous l node
                    cur.val, l.val = l.val, cur.val
                    return
                else:
                    # first time encountering an misplaced node, record it and
                    # move on. 'r' will handle the edge case when two
                    # consecutive nodes in the sorted iteration are swapped, in
                    # which case the second misplacement cannot be detected in
                    # the iteration.
                    l, r = prev, cur
            # record 'prev' for the next iteration
            # move pointer to handle the right sub-tree 
            prev, root = cur, cur.right
           
    # the edge case
    l.val, r.val = r.val, l.val

