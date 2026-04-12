class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        s = sum(nums)
        # It has to be abs!!!
        if abs(target) > s or (target + s) % 2 != 0:
            return 0

        p = (target + s) // 2
        dp = [0] * (p + 1)
        dp[0] = 1

        for num in nums:
            for j in range(p, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[p]