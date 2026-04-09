class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        buy = 2*31-1
        for p in prices:
            buy = min(buy, p)

            profit = max(profit, p - buy)

        return profit
