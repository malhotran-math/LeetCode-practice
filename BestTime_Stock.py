class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse = True):
            return 0
        else: 
            profit = 0
            buy_price = max(prices)
            for p in prices: 
                buy_price = min(buy_price,p)
                profit = max(profit, p-buy_price)
            return profit
