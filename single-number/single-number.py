from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        rev = {v:k for k, v in cnt.items()}
        return rev[1]
        