class Solution:
    def prd(self, nums: list[int]) -> list[int]:
        
        fprod = [1]
        for i in range(0,len(nums)-1):
            fprod.append(fprod[i] * nums[i])

        rprod = [1 for _ in range(len(nums))]
        for i in range(len(nums)-1,0,-1):
            rprod[i-1] = rprod[i] * nums[i]
        
        return [fprod[i] * rprod[i] for i in range(len(nums))]
    