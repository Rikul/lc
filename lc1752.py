class Solution:

    # 1752. Check if Array Is Sorted and Rotated
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        l = [i for i,x in enumerate(nums) if x == min(nums)] 

        not_found = 0
        for x in l:
            prev = 0
            for i in range(n):
                y = nums[(x + i) % n]
                if prev > y:
                    not_found += 1
                    break
                prev = y

        return not_found < len(l)

s = Solution
print(s.check(s,[6,7,2,7,5]))
print(s.check(s,[6,10,6]))
print(s.check(s,[1,1,1]))
print(s.check(s,[3,4,5,1,2]))
print(s.check(s,[2,1,3,4]))
print(s.check(s,[1,2,3]))
