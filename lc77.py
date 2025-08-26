from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
            
        def backtrack(N: int, K: int, start: int, curr: List[int], result: List[List[int]]):
            if len(curr) == K:
                result.append(curr[:])
                return

            for i in range(start+1,N+1):
                curr.append(i)
                backtrack(N, K, i, curr, result)
                curr.pop()


        result = []
        backtrack(n,k,0,[], result)

        return result



if __name__ == "__main__":
    sol = Solution()
    result = sol.combine(5,3)
    print(result)