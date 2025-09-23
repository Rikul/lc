class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        rev1 = [int(x) for x in version1.split(".")]
        rev2 = [int(x) for x in version2.split(".")]

        maxlen = max(len(rev1), len(rev2))
        rev1.extend([0] * (maxlen - len(rev1)))
        rev2.extend([0] * (maxlen - len(rev2)))

        for i,n in enumerate(rev1):
            if rev1[i] < rev2[i]:
                return -1
            elif rev1[i] > rev2[i]:
                return 1
             

        return 0