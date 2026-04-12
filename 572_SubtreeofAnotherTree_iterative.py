# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.issame(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def issame(self, root:Optional[TreeNode], subRoot: Optional[TreeNode]):
        p = root
        q = subRoot
        # Both are empty
        if not p and not q:
            return True
        # One is empty while the other one is not.
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.issame(p.left,q.left) and self.issame(p.right,q.right)

