from typing import List

class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        matches = set()
        candidates.sort()

        def backtrack(curr : List[int], curr_sum : int, start: int = 0):
                        
            if curr_sum == target:
                matches.add(tuple(sorted(curr)))
                print(curr)
                return
           
            for i in range(start,len(candidates)):
                n = candidates[i]
                if curr_sum + n <= target:
                    backtrack(curr + [n], curr_sum + n, start + 1)
        
        backtrack([], 0)

        return [list(t) for t in matches]

    

if __name__ == "__main__":
    sol = Solution()
    #list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5]
    list2 = [10,1,2,7,6,1,5] # [1,1,2,5,6,7,10]
    result = sol.combinationSum2(list2,8)
    print(result)
    
