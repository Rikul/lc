#include <vector>

using namespace std;


class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> matrix(n, vector<int>(n,0));

        int dr = 0, dc = 1;
        int r = 0, c = 0;
        int t = 1;

        while(r < n && r >= 0 && c < n && c >= 0 && matrix[r][c] == 0) {

            matrix[r][c] = t++; 

            if (dr > 0 && (r + dr >= n || matrix[r+dr][c] != 0)) {
                dr = 0;
                dc = -1;
            } else if (dr < 0 && (r + dr < 0 || matrix[r+dr][c] != 0)) {
                dr = 0;
                dc = 1;
            } else if (dc > 0 && (c + dc >= n || matrix[r][c+dc] != 0)) {
                dr = 1;
                dc = 0;
            } else if (dc < 0 && (c + dc < 0 || matrix[r][c+dc] != 0)) {
                dr = -1;
                dc = 0;
            }

            r += dr;
            c += dc;
        }
                
        return matrix;
    }
};