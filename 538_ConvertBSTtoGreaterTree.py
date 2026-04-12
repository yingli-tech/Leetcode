# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0

        def order(node):
            if not node:
                return 0
            # Update right child at first
            order(node.right)
            # Accumulate the value for each node
            self.sum += node.val
            # Update left child 
            node.val = self.sum

            order(node.left)

        order(root)
        
        return root