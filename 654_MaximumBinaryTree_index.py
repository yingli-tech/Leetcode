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

            root_val = max(nums[start:end + 1])
            root = TreeNode(root_val)
            # Look for the index in an appointed interval
            idx = nums.index(root_val, start, end + 1)

            root.left = cons(start, idx - 1)
            root.right = cons(idx + 1, end)

            return root
        
        return cons(0, len(nums) - 1)
        

