class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        if not prices:
            return 0
        
        buy = [float('-inf')] * k
        sell = [0] * k

        for price in prices:
            
            for i in range(0, k):
                if i == 0:
                    buy[i] = max(buy[i], -price)
                else:
                    buy[i] = max(buy[i], sell[i-1] - price)
                
                sell[i] = max(sell[i], buy[i] + price)

        return sell[-1]
