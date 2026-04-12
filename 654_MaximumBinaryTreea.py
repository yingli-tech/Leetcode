# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def cons(start, end):
            if start > end:
                return 

            new = nums[start:end]

            root_val = max(new)
            root = TreeNode(root_val)

            idx = new.index(root_val)

            root.left = self.constructMaximumBinaryTree(0, idx)
            root.right = self.constructMaximumBinaryTree(idx + 1, end)

            return root
        
        return cons(0, len(nums) - 1)
        

