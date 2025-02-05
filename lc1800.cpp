#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
// LC1800 - Maximum Ascending Subarray Sum
    int maxAscendingSum(vector<int>& nums) {
        int sum = nums[0];
        int max_sum = sum;

        if (nums.size() == 1) 
            return sum;

        for(int i=1; i < nums.size(); i++) {
            if (nums[i-1] >= nums[i]) {
                max_sum = max(sum,max_sum);
                sum = nums[i];
            } else {
                sum += nums[i];
            }
        }

        return max(sum,max_sum);
    }
};