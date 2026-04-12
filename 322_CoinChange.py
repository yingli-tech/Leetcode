class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [inf] * amount

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x-coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1