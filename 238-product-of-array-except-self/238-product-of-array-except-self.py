class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        # if len(nums) == 1:
        #     return [0]
        n = 1
        for i in range(len(nums)):
            result.append(n)
            n *= nums[i]
        n = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= n
            n *= nums[i]
        return result