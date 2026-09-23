class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         return True
        return False

        