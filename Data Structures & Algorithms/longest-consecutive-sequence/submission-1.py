class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        all_set = set()
        for n in nums:
            all_set.add(n)

        length = 0
        max_length = 0

        for n in nums:
            if n - 1 not in all_set:
                length = 1
                while n + length in all_set:
                    length += 1
                max_length = max(max_length, length)

        return max_length

    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_count = 1
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] + 1 == nums[i + 1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count