# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Global maximum initiates as negative infinitive
        self.max_sum = float('-inf')  

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                # This step is very important because it can avoid parameter None in the function max.
                return 0
            # return the maximum path sum of the subtree rooted at 'node'
            # If subtree path sum is negative, do not add it, take max(0, …)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Update global maximum: path could be left + current + right
            self.max_sum = max(self.max_sum, left + right + node.val)

            # Return to parent: current node + max single side path from left or right
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum