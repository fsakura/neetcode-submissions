class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        print("".join(res))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # inside_str = False
        # for i, c in enumerate(s):
        while i < len(s):
            tmp_str = ""
            while s[i] != '#':
                tmp_str += s[i]
                i += 1
            length = int(tmp_str)
            i += 1
            index = i
            tmp_str = ""
            while i < index + length:
                tmp_str += s[i]
                i += 1
            res.append(tmp_str)

        return res
