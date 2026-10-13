class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, res, 0, [])
        return res

    def backtrack(self, nums, res, start, comb):
        # if comb:
        res.append(comb[:])
        
        for i in range(start, len(nums)):
            comb.append(nums[i])
            self.backtrack(nums, res, i + 1, comb)
            comb.pop()