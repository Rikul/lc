#include <vector>

using namespace std;

class Solution {
public:
    
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        const int OUT = -10000;

        vector<int> result = {};
        int dr = 0, dc = 1;
        int r = 0, c = 0;

        while(r < m && r >= 0 && c < n && c >= 0 && matrix[r][c] != OUT) {
            result.push_back(matrix[r][c]);
            matrix[r][c] = OUT; 

            if (dr > 0 && (r + dr >= m || matrix[r+dr][c] == OUT)) {
                dr = 0;
                dc = -1;
            } else if (dr < 0 && (r + dr < 0 || matrix[r+dr][c] == OUT)) {
                dr = 0;
                dc = 1;
            } else if (dc > 0 && (c + dc >= n || matrix[r][c+dc] == OUT)) {
                dr = 1;
                dc = 0;
            } else if (dc < 0 && (c + dc < 0 || matrix[r][c+dc] == OUT)) {
                dr = -1;
                dc = 0;
            }

            r += dr;
            c += dc;
        }

        return result;
    }
};