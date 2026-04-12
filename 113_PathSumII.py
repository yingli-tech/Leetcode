# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path,value):
            if not node:
                return []
            value += node.val
            path.append(node.val)
            if value == targetSum and not node.left and not node.right:
                res.append(path[:])
            else:
                dfs(node.right, path, value)
                dfs(node.left,path, value)
            
            path.pop()
            
        dfs(root, [], 0)

        return res