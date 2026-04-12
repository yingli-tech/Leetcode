class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        if nums[middle] > target: # After executing the codes above, the order of nums[middle] and target hasn't been determined
                                    # An extra comparison is needed because the return index relies on this determined order
            return middle  
        else:
            return middle + 1