# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = float("-inf")

        def inorder(node):
            if not node:
                return True
            
            if not inorder(node.left):
                return False
            
            if self.pre >= node.val:
                return False
            
            self.pre = node.val

            return inorder(node.right)
        
        return inorder(root)


