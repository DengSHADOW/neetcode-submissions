class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 1000
        profit = 0

        for sell in prices:
            if sell<buy:
                buy=sell
            else:
                profit = max(sell-buy, profit)
        return profit