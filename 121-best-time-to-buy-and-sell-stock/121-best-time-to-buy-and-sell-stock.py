class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        m = sys.maxsize
        for price in prices:
            m = min(m, price)
            profit = max(profit, price-m)
        return profit