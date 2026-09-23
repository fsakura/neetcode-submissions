class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prod = 1
        for i in range(0, len(nums) - 1):
            prod *= nums[i]
            res[i + 1] = prod
        
        res2 = [1] * len(nums)
        prod = 1
        for i in range(len(nums) - 1, 0, -1):
            prod *= nums[i]
            res[i - 1] *= prod
        return res
        # return [x * y for x, y in zip(res, res2)]