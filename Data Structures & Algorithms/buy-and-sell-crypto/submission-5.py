class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 2**31 - 1
        sell = -2**31
        profit = 0
        for p in prices:
            bought_today = False
            if p < buy:
                buy = p
                sell = -2**31
                bought_today = True
            elif p > sell:
                sell = p
            
            if not bought_today:
                profit = max(profit, (sell - buy))
        return profit if profit > 0 else 0

            
