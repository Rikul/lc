

class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        idx = {i for i in range(len(boxes)) if boxes[i] == '1'}
        result = []
        
        for i in range(len(boxes)):
            r = sum(abs(i-j) for j in idx)
            result.append(r)

        return result
    
"""
# Github Copilot Optimized solution
from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        count = 0
        operations = 0
        
        # Left to right pass
        for i in range(n):
            result[i] += operations
            count += int(boxes[i])
            operations += count
        
        count = 0
        operations = 0
        
        # Right to left pass
        for i in range(n-1, -1, -1):
            result[i] += operations
            count += int(boxes[i])
            operations += count
        
        return result

sol = Solution()
print(sol.minOperations("001011")) 
"""