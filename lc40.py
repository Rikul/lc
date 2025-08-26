from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        matches = []
        candidates.sort()

        def backtrack(curr : List[int], start_idx : int, curr_sum : int):
                        
            if curr_sum == target:

                if curr not in matches:
                    matches.append(curr[:])
                else:
                    print(curr)

                return
            
            for i in range(start_idx, len(candidates)):
                n = candidates[i]
                if curr_sum + n <= target:
                    backtrack(curr + [n], i+1, curr_sum + n)

        
        backtrack([],0 ,0)

        return matches
    

if __name__ == "__main__":
    sol = Solution()
    result = sol.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5],15)
    print(result)
    
