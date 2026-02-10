#include <vector>
#include <unordered_set>
#include <map>
#include <iostream>
#include <functional>

using namespace std;

class Solution {

    unordered_set<char> get_union(const unordered_set<char>& set1, 
                              const unordered_set<char>& set2,
                              const unordered_set<char>& set3) {
        unordered_set<char> result = set1;  // Start with set1
        result.insert(set2.begin(), set2.end());  // Add set2
        result.insert(set3.begin(), set3.end());  // Add set3
        return result;
    }

public:

    void solveSudoku(vector<vector<char>>& board) {

        const int BOARD_SIZE = 9;
        const unordered_set<char> ALL_DIGITS = {'1','2','3','4','5','6','7','8','9'};

        vector<pair<int,int>> empty_cells;
        map<pair<int,int>, unordered_set<char>> unused;
        map<int, vector<pair<int,int>>> box_cells;

        vector<unordered_set<char>> in_row(9);
        vector<unordered_set<char>> in_col(9);
        vector<unordered_set<char>> in_box(9);
    
        for (int i = 0; i < BOARD_SIZE; i++) {
            for(int j = 0; j < BOARD_SIZE; j++) {
                int boxn = 3 * ((int)i / 3) + ((int) j / 3);
                box_cells[boxn].push_back({i,j});

                if (board[i][j] == '.') {
                    empty_cells.push_back({i,j}); 
                    unused[{i,j}] = ALL_DIGITS;
                } else {
                    in_row[i].insert(board[i][j]);
                    in_col[j].insert(board[i][j]);
                    in_box[boxn].insert(board[i][j]);
                }
            }
        }

        bool changed = true;
        while (changed) {

            changed = false;
            for(int i = empty_cells.size() - 1; i >= 0; i--) {
                auto cell = empty_cells[i];
                int r = cell.first; 
                int c = cell.second;
                int boxn = 3 * ((int)r / 3) + ((int) c / 3);

                if (board[r][c] != '.') {
                    empty_cells.erase(empty_cells.begin() + i);
                    continue;
                }

                int unused_count = unused[cell].size();
                
                for(char d: get_union(in_row[r], in_col[c], in_box[boxn]))
                    unused[cell].erase(d);

                if (unused_count != unused[cell].size()) {
                    changed = true;
                }

                bool found = false;
                char found_digit = '.';

                if (unused[cell].size() == 1) {
                    // found solution for this cell.
                    found = true;
                    found_digit = *unused[cell].begin();
                } else {
                    // Check if any digits in cell can only be used here.
                    for(char d: unused[cell]) {
                        bool has_in_other = false;
                        for(auto celltmp: box_cells[boxn]) {
                            if (celltmp.first != r || celltmp.second != c) {
                                // Its in the box or can be used in other cells of the box
                                if ((unused[celltmp].find(d) != unused[celltmp].end()) || 
                                        (in_box[boxn].find(d) != in_box[boxn].end())) {
                                    has_in_other = true;
                                    break;
                                }
                            }
                        }
                        
                        if (! has_in_other) {
                            found = true;
                            found_digit = d;
                            break;
                        }
                    }
                }

                if (found) {
                    in_row[r].insert(found_digit);
                    in_col[c].insert(found_digit);
                    in_box[boxn].insert(found_digit);
                    board[r][c] = found_digit;
                    unused.erase(cell);
                    changed = true;
                    empty_cells.erase(empty_cells.begin() + i);
                }

            }

        } 

        std::function<void(int)> bt = [=, &bt, &board, &unused, &empty_cells] (int x) {

            if (x >= empty_cells.size()) {
                return;
            }
        
            for(int i=x; i<empty_cells.size(); i++) {
                pair<int,int> cell = empty_cells[i];
                int r = cell.first;
                int c = cell.second;
                unordered_set<char> unused_digits = unused[cell];
                
                for(char d: unused_digits) {
                    bool can_use = false;

                    for(char ch: in_row[r]) {
                        if (ch == d) {
                            can_use = false;
                            break;
                        } 
                    } 

                    board[r][c] = d;
                    bt(i+1);
                    //board[cell.first][cell.second] = '.';
                }
            }

        };

       // bt(0);

        cout << endl << endl;
        for (int i = 0; i < BOARD_SIZE; i++) {
            for(int j = 0; j < BOARD_SIZE; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }

        return;
    }
};

int main() {
    Solution s;
    vector<vector<char>> board = {
                                {'.','.','9','7','4','8','.','.','.'},
                                {'7','.','.','.','.','.','.','.','.'},
                                {'.','2','.','1','.','9','.','.','.'},
                                {'.','.','7','.','.','.','2','4','.'},
                                {'.','6','4','.','1','.','5','9','.'},
                                {'.','9','8','.','.','.','3','.','.'},
                                {'.','.','.','8','.','3','.','2','.'},
                                {'.','.','.','.','.','.','.','.','6'},
                                {'.','.','.','2','7','5','9','.','.'}};

    s.solveSudoku(board);
    return 0;
}