class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = inf
        n = len(nums)
        if not nums:
            return 0
        
        left = 0
        sum = 0

        # sliding window problem
        for right in range(n):
            sum += nums[right]
            while (sum >= target):
                length = right - left + 1
                min_length = min(length, min_length)
                sum -= nums[left]
                left += 1
        
        return 0 if min_length == inf else min_length