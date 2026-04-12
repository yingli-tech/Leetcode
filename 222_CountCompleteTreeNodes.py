# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = root
        h_l = 0
        while left:
            h_l += 1
            left = left.left
        
        right = root
        h_r = 0
        while right:
            h_r += 1
            right = right.right
        
        if h_r == h_l:
            return pow(2,h_r) - 1 
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)