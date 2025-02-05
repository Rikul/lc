#include <vector>
#include <iostream>
#include <algorithm>

class Solution {
public:
    // LC3105 - Longest Monotonic Subarray
    int longestMonotonicSubarray(std::vector<int>& nums) {
        int run = 1;
        int longest_run = run;

        if (nums.size() <= 1) 
            return run;

        bool is_increasing = nums[1] > nums[0];
        for(int i=1; i<nums.size(); i++) {
            if ((nums[i] > nums[i-1] && is_increasing) || (nums[i] < nums[i-1] && !is_increasing)) {
                run += 1;
            } else {
                is_increasing = nums[i] > nums[i-1];
                longest_run = std::max(longest_run, run);
                run = (nums[i] == nums[i-1]) ? 1 : 2;
            }
        }
        
        return std::max(longest_run,run);
    }
};
