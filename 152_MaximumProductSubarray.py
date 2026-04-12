class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_dp = [0] * n
        max_dp = [0] * n
        min_dp[0] = max_dp[0] = max1 = nums[0]

        for i in range(1, n):
            max_dp[i] = max(nums[i], min_dp[i-1] * nums[i], max_dp[i-1] * nums[i])
            min_dp[i] = min(nums[i], min_dp[i-1] * nums[i], max_dp[i-1] * nums[i])
            max1 = max(max1, max_dp[i])

        return max1