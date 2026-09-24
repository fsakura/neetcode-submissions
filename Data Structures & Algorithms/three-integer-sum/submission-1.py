class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        prev = None
        for i, e in enumerate(nums):
            if e == prev:
                continue
            prev = e
            target = -e
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    res.append([e, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res