class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        for sell in prices:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        return profit