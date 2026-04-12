# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
    
        stack = [root]
        result = []
    
        while stack:
            node = stack.pop()  # Middle
            result.append(node.val)
        
            if node.right:      # Rightchild 
                stack.append(node.right)
            if node.left:       # Leftchild
                stack.append(node.left)
    
        return result    