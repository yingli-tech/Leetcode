class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                start = middle - 1
                while start >= 0 and nums[start] == nums[middle]:   # mixed this symbol "and" with "&", so the error existed
                    start -= 1
                end = middle + 1
                while end < len(nums) and nums[end] == nums[middle]:
                    end += 1
                return [start + 1, end - 1]
        return [-1, -1]  