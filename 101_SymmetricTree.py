# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res = []
        q = deque([root])

        while q:
            # Initial the current_level each time 
            current_level = []
            size = len(q)
            for _ in range(size):
                n = q.popleft()
                if n:
                    current_level.append(n.val)
                    # Without considering whether the child is None or not
                    q.append(n.left)
                    q.append(n.right)
                # Input the 'None' in the current_level to ensure this tree has a symmetric structure
                # Not just symmetric values
                else:
                    current_level.append(None)
            left = 0
            right = size - 1
            while (left <= right):
                if current_level[left] == current_level[right]:
                    left += 1
                    right -= 1
                else:
                    return False

        return True        


        