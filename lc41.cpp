#include <unordered_map>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        unordered_map<int, int> ncount;
        
        for(int i=0; i<nums.size(); i++) {
            ncount[nums[i]]++;
        }

        for(int i=1; i < pow(2,31); i++) {
            if (ncount[i] == 0) {
                return i;
            }
        }

        return 0;
    }
};


int main() {
    Solution *sol = new Solution();
    vector<int> nums = {100000, 3, 4000, 2, 15, 1, 99999};
    cout << sol->firstMissingPositive(nums) << endl;;

    return 0;
}