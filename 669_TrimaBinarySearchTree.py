# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        # If current node is lower than low, entire left subtree doesn't fall within the interval → go to right subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # If current node is greater than high, entire right subtree doesn't fall within the interval → go to left subtree
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # Current node is within the interva → keep it and regress to trim subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root