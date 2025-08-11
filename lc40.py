from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()  # Sort to handle duplicates and for easier combination generation

        matches = []
        memo = {}

        def backtrack(curr : List[int], start_idx : int, curr_sum : int):

            if curr_sum == target:
                #curr.sort()
                if curr not in matches:
                    matches.append(curr)

                return
            
            #print(repr(curr))    

            for i in range(start_idx, len(candidates)):
                n = candidates[i]
                if curr_sum + n <= target:
                    backtrack(curr + [n], i+1, curr_sum + n)
                else:
                    break  # No need to continue if the sum exceeds target

        backtrack([],0 ,0)

        return matches

if __name__ == "__main__":
    sol = Solution()

    candiates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,33,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,44,4,4,4,5,5,5,5,5,5,5,5,5,5,5,49,5,5,5,5,6,6,6,6]
    #candiates = [1,1,2,3,4,5]
    target = 29

    print(sol.combinationSum2(candiates, target))
