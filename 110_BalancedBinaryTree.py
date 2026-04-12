# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]):
            if not node:
                return 0
            hl = height(node.left)
            # Left subtree is not balanced
            if hl == -1:
                return -1
            hr = height(node.right)
            # Right subtree is not balanced
            if hr == -1:
                return -1
            # This tree is not balanced
            if abs(hl-hr) > 1:
                return -1
            return 1 + max(hl, hr)
        return height(root) != -1