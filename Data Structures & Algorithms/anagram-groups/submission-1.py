class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            so = "".join(sorted(s))
            # print(so)
            if so in res:
                vals = res[so]
                vals.append(s)
                res[so] = vals
            else:
                res[so] = [s]
        # print(res)
        return list(res.values())
        