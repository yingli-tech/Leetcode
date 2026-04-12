class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float('-inf')] * k
        sell = [0] * k

        for price in prices:
            
            buy[0] = max(buy[0], -price)
            sell[0] = max(sell[0], buy[0] + price)

            for i in range(1, k):
                buy[i] = max(buy[i], sell[i-1] - price)
                sell[i] = max(sell[i], buy[i] + price)
        
        return sell[-1]