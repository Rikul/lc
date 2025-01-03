class Solution:
    
    def minStartValue(self, nums: list[int]) -> int:
        initialValue = abs(nums[0]) + 1 if nums[0] < 0 else 1
        
        while True:
            stepSum = initialValue
            for n in nums:
                stepSum += n
                if stepSum <= 0:
                    break
            else:
                return initialValue
            
            initialValue += 1