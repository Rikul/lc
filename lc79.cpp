#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <algorithm> 
#include <set>
#include <map>
#include <unordered_map>
#include <tuple>

using namespace std;

class Solution {

    vector<vector<char>> _board;
    string _word;
    int m, n;

    bool search(int r, int c, int p) {

        if (_board[r][c] != _word[p]) return false;
        if (p == _word.size() - 1) return true;

        char save = _board[r][c];
        _board[r][c] = '\0';

        vector<pair<int,int>> adj = { {r-1,c}, {r+1,c}, {r,c-1}, {r,c+1} };
        for(auto pos: adj) {
            auto [r1,c1] = pos;
        
            if (0 <= r1 && r1 < m && 0 <= c1 && c1 < n && _board[r1][c1] != '\0') {        
                if (search(r1,c1,p+1))
                    return true;
            }
        }
        
        _board[r][c] = save;
        return false;
    }

public:

    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();
        vector<pair<int,int>> start_positions;

        _board = board;
        _word = word;
        
        // early exit
        if ((int)word.size() > m * n) return false;
        unordered_map<char,int> cnt;
        for (auto &row: board) 
            for (char ch: row) cnt[ch]++;

        for (char ch: word) 
            if (--cnt[ch] < 0) 
                return false; 

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if (board[i][j] == word[0] && search(i,j,0))
                    return true;
            }
        }
        
        return false;        
    }
};

int main() {
    Solution s;
    /*
    vector<vector<char>> board = {  {'Z','B','C','E'},
                                    {'S','F','C','S'},
                                    {'A','D','E','E'},
                                    {'W','Z','Z','Z'}};

    */

    /*
    vector<vector<char>> board =    {{'A','A','A','A','A','A'},
                                    {'A','A','A','A','A','A'},
                                    {'A','A','A','A','A','A'},
                                    {'A','A','A','A','A','A'},
                                    {'A','A','A','A','A','B'},
                                    {'A','A','A','A','B','A'}};

    */

    vector<vector<char>> board =   {{'A','B','C','E'},
                                    {'S','F','E','S'},
                                    {'A','D','E','E'}};
    
    //s.exist(board, "SEE");
    //s.exist(board,"AAAAAAAAAAAAABB");
    bool found = s.exist(board, "ABCESEEEFS");
    if (found) 
        cout << "Solution found" << endl;
}