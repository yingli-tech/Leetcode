class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right -left) // 2
            if nums[middle] < target:
                left = middle + 1 # The target is in the right interval
            elif nums[middle] > target:
                right = middle - 1 # The target is in the left interval
            else:
                return middle
        return -1
