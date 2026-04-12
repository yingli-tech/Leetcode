# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        def dfs(node, value):
            if not node:
                return False
            value += node.val
            
            if not node.right and not node.left:
                return value == targetSum
            return dfs(node.right, value) or dfs(node.left, value)

        
        return dfs(root, 0)
            