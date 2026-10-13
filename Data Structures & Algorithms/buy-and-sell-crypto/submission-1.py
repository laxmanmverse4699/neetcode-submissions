class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # buy = 0
        # sell = 1
        
        # while sell < len(prices):
        #     if prices[buy] < prices[sell]:
        #         profit = prices[sell] - prices[buy]
        #         max_profit = max(max_profit, profit)
        #     else:
        #         buy = sell
        #     sell += 1
        # return max_profit
            
        profit = 0
        min_val = float('inf')

        for i in range(len(prices)):
            min_val = min(prices[i], min_val)
            profit = max(profit, prices[i] - min_val)
        return profit
        