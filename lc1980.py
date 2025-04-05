from collections import Counter

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        cnt = Counter(nums)

        n = len(nums[0])
        found = None

        def bin_perm(curr):
            nonlocal found,cnt

            if len(curr) == n:
                bin_str = "".join(curr)  
                if cnt[bin_str] == 0:
                    found = bin_str              
                return
            
            if found: 
                return

            for c in ['0','1']:
                curr += c
                bin_perm(curr)
                curr.pop()

        bin_perm([])

        return found
    
s = Solution()
print(s.findDifferentBinaryString(["0101","1010"])) # 11