# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque([root])
        res = []
        
        while q:
            size = len(q)
            # To record the values of the current level
            current_level = []
            
            for _ in range(size):
                n = q.popleft()
                # Append the value of the node when the node is popped
                current_level.append(n.val)
                
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            res.append(current_level)
        
        return res