# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        # From the condition, we know this is an inorder binary tree.
        def dfsi(node):
            if not node:
                return
            dfsi(node.left)
            res.append(node.val)
            dfsi(node.right)
        dfsi(root)
        return res[k - 1]
        