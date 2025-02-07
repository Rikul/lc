#include <vector>
#include <unordered_map>


using namespace std;


class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        unordered_map<int,int> balls;   // store color for each ball.
        unordered_map<int,int> colors;  // count for each colors
        vector<int> result;
        int distinct = 0;

        for (const auto& query : queries) {
            int ball = query[0];
            int color = query[1];
            int& old_color = balls[ball];

            if (old_color != color) {
                if (colors[color] == 0) {
                    distinct++;
                }

                if (old_color != 0) {
                    colors[old_color]--;
                    if (colors[old_color] == 0) {
                        distinct--;
                    }
                }

                colors[color]++;
                old_color = color;
            }

            result.push_back(distinct);
        }

        return result;
    }
};