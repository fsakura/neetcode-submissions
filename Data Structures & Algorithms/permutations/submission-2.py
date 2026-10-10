class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        self.dfs(nums, perms, [], set())
        return perms
    
    def dfs(self, nums, perms, buffer, is_visited):
        if len(buffer) == len(nums): 
            perms.append(buffer[:])
        
        for num in nums:
            if not num in is_visited:
                buffer.append(num)
                is_visited.add(num)
                self.dfs(nums, perms, buffer, is_visited)
                buffer.pop()
                is_visited.remove(num)