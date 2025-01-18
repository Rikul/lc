class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:

        result = []
        for i in range(len(A)):
            x = len(set(A[0:i+1]).intersection(set(B[0:i+1])))
            result.append(x)

        return result

import cProfile,random

def test_function():
    #A = [1, 2, 3, 4, 5]
    #B = [5, 4, 3, 2, 1]
    A = list(range(1, 21))
    B = list(range(1, 21))
    random.shuffle(A)
    random.shuffle(B)

    solution = Solution()
    solution.findThePrefixCommonArray(A, B)

cProfile.run('test_function()')