from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()        

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_start, prev_end = merged[-1]

            if intervals[i][0] >= prev_start and intervals[i][1] <= prev_end:
                continue 
            elif intervals[i][0] > prev_end:
                merged.append(intervals[i])
            elif intervals[i][0] >= prev_start and intervals[i][1] > prev_end:
                merged[-1] = [prev_start, intervals[i][1]] 

        return merged