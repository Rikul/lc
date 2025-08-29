#include <vector>
#include <cstdio>

using namespace std;

class Solution {
    int nr, nc;

public:

    void setRowZero(vector<vector<int>>& matrix, int row) {
        for(int c = 0; c < this->nc; c++) {
            matrix[row][c] = 0;
        }
    }

    void setColumnZero(vector<vector<int>>& matrix, int column) {
        for(int r = 0; r < this->nr; r++) {
            matrix[r][column] = 0;
        }
    }

    void setZeroes(vector<vector<int>>& matrix) {
        this->nr = matrix.size();
        this->nc = matrix[0].size();

        vector<int> rows(nr, -1);
        vector<int> cols(nc, -1);

        for(int i=0; i < this->nr; i++) {
            for(int j=0; j < this->nc; j++) {
                if (matrix[i][j] == 0) {
                    rows[i] = 0;
                    cols[j] = 0;
                }
            }
        }    

        for(int i=0; i < this->nr; i++) {
            if (rows[i] == 0) {
                setRowZero(matrix,i);
            }
        }

        for(int j=0; j < this->nc; j++) {
            if (cols[j] == 0) {
                setColumnZero(matrix,j);
            }
        }
    }
};

int main() {
    Solution* s = new Solution();
    vector<vector<int>> matrix = {
        {1,1,1},
        {1,0,1},
        {1,1,1}
    };
    s->setZeroes(matrix);

    for(auto row : matrix) {
        for(auto col : row) {
            printf("%d ", col);
        }
        printf("\n");
    }
    return 0;

}