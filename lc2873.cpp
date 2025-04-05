#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
    long long maximumTripletValue(std::vector<int>& nums) {
        long long x = 0;

        for(int i=0; i < nums.size(); i++) {
            for(int j=i+1; j < nums.size(); j++) {
                for(int k=j+1; k < nums.size(); k++) {
                    long long tmp = ((long)nums[i] - (long)nums[j]) * nums[k];
                    x = tmp > x ? tmp : x;
                }
            }
        }

        return x;
    }
};