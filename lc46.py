from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        mutations = []

        def bt(curr: List[int], from_list: List[int]):

            for i,n in enumerate(from_list):
                avail = from_list[0:i] + from_list[i+1:len(from_list)]

                if len(curr + [n]) == len(nums): 
                    mutations.append(curr + [n])

                if len(avail):
                    bt(curr + [n], avail)



        bt([], nums)

        return mutations
    

if __name__ == "__main__":
    sol = Solution()
    result = sol.permute([1,3,5,7])
    print(result)
