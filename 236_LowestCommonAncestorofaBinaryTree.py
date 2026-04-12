# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root
        # Search for p or q in left subtree and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # If the nodes exist in two subtrees, which means current node is the lowest ancestor node. 
        if left and right:
            return root

        # If one node exists in one subtree while the other node is not in the other subtree, return the subtree has the node. 
        # If both subtrees don't have the node, return None （there is no the lowest common ancestor）.
        return left if left else right
