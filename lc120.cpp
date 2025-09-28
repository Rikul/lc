
#include <vector>

using namespace std;

class Solution {
public:

    int minimumTotal(vector<vector<int>>& triangle) {

        int nrows = triangle.size();
        vector<vector<int>> dp(nrows, vector<int>(nrows));

        dp[0][0] = triangle[0][0];
        for(int i = 1; i < nrows; i++) {
            for(int j = 0; j < triangle[i].size(); j++) {
                if (j == 0)
                    dp[i][j] = dp[i-1][j] + triangle[i][j];
                else if (j == triangle[i].size() - 1) 
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j];
                else 
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j];
            }
        }

        auto min_it = std::min_element(dp[nrows-1].begin(), dp[nrows-1].end());
        return *min_it;

    }
};