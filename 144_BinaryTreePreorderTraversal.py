# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # Depth-First Search
        # The three depth-first traversal methods—preorder, inorder, and postorder—are essentially just different placements of the three steps below. Inorder is left-root-right, and postorder is left-right-root.
        def dfs(node):
            if not node:
                return
            res.append(node.val)     # Root
            dfs(node.left)           # Leftchild
            dfs(node.right)          # Rightchild

        dfs(root)
        return res        

        