class Solution:
    # 3151 Special Array I
    def isArraySpecial(self, nums: List[int]) -> bool:
        return len(nums) == 1 or all(nums[i] % 2 != nums[i+1] % 2 for i in range(len(nums)-1))
        