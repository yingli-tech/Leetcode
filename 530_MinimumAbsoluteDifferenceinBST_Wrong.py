# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return
            if node.left:
                res.append(abs(node.left.val - node.val))
                dfs(node.left)
            if node.right:
                res.append(abs(node.right.val - node.val))
                dfs(node.right)
        
        dfs(root)

        return min(res) if res else 0