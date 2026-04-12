class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        sold = rest = 0

        for price in prices:
            pre_hold = hold
            pre_rest = rest
            pre_sold = sold
            # Only the hold and rest state are possible former states of a hold state.
            hold = max(pre_hold, rest - price)
            # Before the sold state, it must be hold state.
            sold = hold + price
            # Only the sold and rest state are possible former states of a rest state.
            rest = max(pre_rest, pre_sold)

        return max(sold, rest)

