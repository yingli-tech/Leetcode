# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = deque([p])
        p2 = deque([q])

        while p1:
            current_level_1 = []
            current_level_2 = []
            size1 = len(p1)
            size2 = len(p2)
            if size1 != size2:
                return False
            
            for _ in range(size1):
                n = p1.popleft()
                if n:
                    current_level_1.append(n.val)
                    p1.append(n.left)
                    p1.append(n.right)
                else:
                    current_level_1.append(None)

            for _ in range(size1):
                n = p2.popleft()
                if n:
                    current_level_2.append(n.val)
                    p2.append(n.left)
                    p2.append(n.right)
                else:
                    current_level_2.append(None)

            for i in range(size1):
                if current_level_1[i] != current_level_2[i]:
                    return False

        return True           