# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # Actually no need to check leaf and right node case, because the exchange function doesn't care about the node type. 
        if not root.left and not root.right:
            return root

        def exchange(node):
            if not node:
                return 
            temp = node.left
            node.left = node.right
            node.right = temp
            
            exchange(node.left)
            exchange(node.right)

        exchange(root)

        return root