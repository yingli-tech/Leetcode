from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
            print(nums[i])
        nums.sort()
        return nums
    
solution = Solution()
arr = [-4, -1, 0, 3, 10]
result = solution.sortedSquares(arr)
print(result) 