class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        index_map = {}
        l = 0
        for r in range(len(s)):
            if s[r] in index_map:
                l = max(l, index_map[s[r]] + 1)
            index_map[s[r]] = r
            res = max(res, r - l + 1)
        return res

        