class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1

        profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                curr = prices[sell] - prices[buy]
                profit = max(profit,curr)
            else:
                 buy = sell
            sell+=1
        return profit
