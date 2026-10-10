class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.back_track(nums, res, [], set())
        return res

    def back_track(self, nums, res, perm, is_visited):
        if len(perm) == len(nums):
            res.append(perm[:])
        
        for num in nums:
            if num not in is_visited:
                print(perm)
                perm.append(num)
                is_visited.add(num)
                self.back_track(nums, res, perm, is_visited)
                perm.remove(num)
                is_visited.remove(num)

