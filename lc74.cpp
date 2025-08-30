#include <vector>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int nr = matrix.size();
        int nc = matrix[0].size();
        int sz = nr * nc;

        int left = 0; 
        int right = sz - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            int row = mid / nc;
            int col = mid % nc;

            if (matrix[row][col] == target) 
                return true;
            else if (matrix[row][col] < target) 
                left = mid + 1;
            else 
                right = mid - 1;
        }   

        return false;
    }
};