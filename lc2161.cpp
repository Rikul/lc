#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> pivotArray(vector<int>& nums, int pivot) {
            vector<int> lt, gt;
            int p = 0;
    
            for(int i=0; i < nums.size(); i++) {
                if (nums[i] == pivot) p++;
                else if (nums[i] < pivot) lt.push_back(nums[i]);
                else gt.push_back(nums[i]);
            }
    
            lt.insert(lt.end(), p, pivot);
            lt.insert(lt.end(), gt.begin(), gt.end());
            return lt;
        }
    };