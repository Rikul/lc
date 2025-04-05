#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    long long maximumTripletValue(std::vector<int>& nums) {
        std::vector<int> prefix_max, suffix_max;
        int max_temp1 = 0, max_temp2 = 0;
        for(int i=0, j = nums.size() - 1; i < nums.size() && j >= 0; i++, j--) {
            if (nums[i] > max_temp1)
                max_temp1 = nums[i];
            if (nums[j] > max_temp2)
                max_temp2 = nums[j];
            
            suffix_max.insert(suffix_max.begin(), max_temp2);
            prefix_max.push_back(max_temp1);
        }


        return 0;
    }
};

int main() {
    Solution sol;
    std::vector<int> nums = {1,10,3,4,19};
    std::cout << sol.maximumTripletValue(nums) << std::endl;
    return 0;
}