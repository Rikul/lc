from collections import defaultdict
from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
    
        def points(i):
            if i >= len(questions):
                return 0
            
            return max(questions[i][0] + points(i + questions[i][1] + 1), points(i+1))
        
        return points(0)