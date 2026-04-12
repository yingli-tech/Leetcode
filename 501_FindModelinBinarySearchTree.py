# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        self.count = defaultdict(int)

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.count[node.val] += 1
            inorder(node.right)
        
        inorder(root)
        max_f = max(self.count.values())
        
        return [val for val, freq in self.count.items() if freq == max_f]