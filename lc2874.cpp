#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    long long maximumTripletValue(std::vector<int>& nums) {
        std::vector<int> prefix_max;
        std::vector<int>suffix_max;
        long long max_temp1 = 0, max_temp2 = 0;

        prefix_max.resize(nums.size());
        suffix_max.resize(nums.size());

        for(int i=0, j = nums.size() - 1; i < nums.size() && j >= 0; i++, j--) {
            if (nums[i] > max_temp1)
                max_temp1 = nums[i];

            if (nums[j] > max_temp2)
                max_temp2 = nums[j];
            
            prefix_max[i] = max_temp1;
            suffix_max[j] = max_temp2;
        }

        max_temp1 = 0;
        for(int i=1; i < nums.size() - 1; i++) {
            max_temp2 = ((long)prefix_max[i-1] - (long)nums[i]) * suffix_max[i+1];
            if (max_temp2 > max_temp1) 
                max_temp1 = max_temp2;
        } 

        return max_temp1;
    }
};


int main() {
    Solution sol;
    std::vector<int> nums = {1,10,3,4,19};
    std::cout << sol.maximumTripletValue(nums) << std::endl;
    return 0;
}