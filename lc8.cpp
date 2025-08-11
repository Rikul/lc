#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
 int myAtoi(string s) {
        int i = 0;
        bool neg = false;
        string d = "";

        if (s.empty()) return 0;

        while (isspace(s[i])) i++;
        
        if (i >= s.size()) return 0;

        if (s[i] == '-') {
            neg = true;
            i++;
        } else if (s[i] == '+') {
            i++;
        }
            
        if (i >= s.size() || !isdigit(s[i])) {
            return 0;
        }

        while (isdigit(s[i])) {
            d += s[i++];
        }

        if (d.empty())
            return 0;

        i = 0;
        while (d[i] == '0')
            i++;
        
        d.erase(0, i);        
        if (d.empty())
            return 0;


        long long result = 0;
        for (int i = 0; i < d.size(); i++) {
            if (result > (INT_MAX - (d[i] - '0')) / 10) {
                return neg ? INT_MIN : INT_MAX;
            }
            result = result * 10 + (d[i] - '0');
        }
        
        if (result > INT_MAX) {
            return neg ? INT_MIN : INT_MAX;
        }

        if (neg) {
            result = -result;
        }

        return result;;
    }


};

int main(int argc, char **argv) {
    Solution *sol = new Solution();

    vector<string> testCases = {
        "   -042",
        "-91283472332",
        "   +42",
        "   -42abc",
        "abc123",
        "-00000000000000123abc",
        "   + 42",
        "-2147483648",
        "0-1",
        "1337c0d3",
        "words and 987"
    };

    for(int i = 0; i < testCases.size(); i++) {
        cout << testCases[i] << " ";
        int result = sol->myAtoi(testCases[i]);
        cout << result << endl;
    }
    
    return 0;
}

