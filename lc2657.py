class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:

        result = []
        for i in range(len(A)):
            x = len(set(A[0:i+1]).intersection(set(B[0:i+1])))
            result.append(x)

        return result
