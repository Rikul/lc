class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
        res = ""
        
        for i in range(len(s)):
            res += s[i]

            if res.endswith(part):
                res = res[:-len(part)]

        return res