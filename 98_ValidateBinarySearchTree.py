# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Help function: recursive check, pass upper and lower bounds
        def helper(node, low, high):
            if not node:
                return True
            
            # Current node should be in the range of (low, high)
            if not (low < node.val < high):
                return False
            
            # Left subtree: update the high value with current node value
            # Right subtree：update the low value with current node value
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        return helper(root, float("-inf"), float("inf"))
