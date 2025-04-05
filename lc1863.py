from typing import List
from functools import reduce

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Start with an empty subset
        subsets = [[]]
        xor_sum = 0

        # Iterate over each element in the array
        for num in nums:
            # For each existing subset, add the current number to create a new subset
            new_subsets = [subset + [num] for subset in subsets]

            # Add the new subsets to the list of all subsets
            subsets.extend(new_subsets)

        for subset in subsets:
            xor_total = reduce(lambda x, y: x ^ y, subset,0)
            xor_sum += xor_total

        return xor_sum