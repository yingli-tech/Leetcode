# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def seq(node:Optional[TreeNode]):
            if not node:
                return ",null"
            return "," + str(node.val) + seq(node.left) + seq(node.right)


        res1 = seq(root)
        res2 = seq(subRoot)

        return res2 in res1
