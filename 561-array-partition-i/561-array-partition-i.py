class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        pairs = len(nums)
        i = 0
        while i < pairs:
            result += nums[i]
            i += 2
        return result