
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        cntHash = {}
        max_freq = 0
        
        for n in nums:
            cntHash[n] = cntHash.get(n, 0) + 1
            max_freq = max(max_freq, cntHash[n])
        
        cnt = 0
        for n in cntHash:
            if cntHash[n] == max_freq:
                cnt += 1
    
        return cnt * max_freq
        