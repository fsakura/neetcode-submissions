class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_index = 0
        sell_index = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            curr_profit = prices[i] - buy
            if curr_profit > profit:
                sell_index = i
                profit = curr_profit
            
            if prices[i] < buy:
                buy = prices[i]
                buy_index = i
        return profit