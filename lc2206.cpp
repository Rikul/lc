#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    bool dv_array(vector<int>& nums) {
        
        int cnt[1000] = {0};

        if (nums.size() % 2) return false;

        for(int n: nums) {
            cnt[n]++;
        }        

        bool has_pairs = false;
        for(int i=0; i < 1000; i++) {
            if (cnt[i] > 0) {
                if (cnt[i] % 2) {
                    return false;
                } else has_pairs = true;

            }
        }

        return has_pairs;
        
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 2, 3, 4, 5, 6};
    cout << s.dv_array(nums) << endl;
    return 0;
}