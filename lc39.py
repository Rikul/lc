from typing import List

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        matches = set()

        def backtrack(curr : List[int], curr_sum : int):
                        
            if curr_sum == target:
                matches.add(tuple(sorted(curr)))
                return
           
            for n in candidates:
                if curr_sum + n <= target:
                    backtrack(curr + [n], curr_sum + n)
        
        backtrack([], 0)

        return [list(t) for t in matches]


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)
    