from typing import List

from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                d[nums1[i][0]] += nums1[i][1]
            
            if i < len(nums2):
                d[nums2[i][0]] += nums2[i][1]


        res = []
        for k in sorted(d):
            res.append([k,d[k]])

        return res
