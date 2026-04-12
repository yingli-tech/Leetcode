class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = max1 = nums[0]
        
        for i in range(1, len(nums)):
            # dp[i]: The maximum sum of the contiguous subarray ending at nums[i]
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            max1 = max(max1, dp[i])
        
        return max1