# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = float("inf")
        self.pre = None
        
        if not root:
            return 0
        
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            
            if self.pre is not None:
                self.min = min(self.min, node.val - self.pre)
            self.pre = node.val
            inorder(node.right)
        
        inorder(root)

        return self.min