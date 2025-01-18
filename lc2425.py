class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
      
        result = nums1[0]
        for i in range(1,len(nums1)):
            result ^= nums1[i]

        for i in range(0, len(nums2)):
            result ^= nums2[i]

        return result