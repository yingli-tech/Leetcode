# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildtree(left, right):
            if left > right:
                return None
                
            middle = (left + right) // 2
            # Always use the middle value as the root or subroot
            root = TreeNode(nums[middle])

            root.left = buildtree(left, middle - 1)
            root.right = buildtree(middle + 1, right)
            return root
        
        return buildtree(0, len(nums) - 1)
