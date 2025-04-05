from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        res = []
        zeros = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            
            if nums[i] != 0:
                res.append(nums[i])
            else:
                zeros += 1
        
        res += [nums[-1]]
        res += [0] * zeros
    
        return res