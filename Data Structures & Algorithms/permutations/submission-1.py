class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        # for num in nums:
        self.dfs(perms, [], nums, set())
        return perms
    
    def dfs(self, perms, buffer, nums, is_visited):
        if len(buffer) == len(nums): 
            perms.append(buffer[:])
        for num in nums:
            if not num in is_visited:
                buffer.append(num)
                is_visited.add(num)
                self.dfs(perms, buffer, nums, is_visited)
                buffer.pop()
                is_visited.remove(num)
                # print(perms)