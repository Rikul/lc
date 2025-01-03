class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        prefix_sum : list[int] = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i-1] + nums[i])

        result = 0
        for i in range(0, len(nums)-1):
            if prefix_sum[i] >= prefix_sum[len(nums)-1] - prefix_sum[i]:
                result += 1
        return result
