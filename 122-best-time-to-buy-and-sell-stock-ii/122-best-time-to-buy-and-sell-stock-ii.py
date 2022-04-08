class Solution:
    def maxProfit(self, p: List[int]) -> int:
        return sum([max(p[i] - p[i-1], 0) for i in range(1, len(p))])