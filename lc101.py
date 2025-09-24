from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symmetric(lnode: TreeNode, rnode: TreeNode) -> bool:
            
            if lnode is None or rnode is None:
                return lnode == rnode

            if lnode.val != rnode.val:
                return False

            return symmetric(lnode.left, rnode.right) and symmetric(lnode.right, rnode.left)
         

        if root is None:
            return True

        return symmetric(root.left, root.right)
        