#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>

class Solution {
public:

    bool areAlmostEqual(std::string s1, std::string s2) {
        std::unordered_map<char,int> s1_map, s2_map;
        int diff = 0;

        for (int i = 0; i < s1.size(); i++) {
            s1_map[s1[i]]++;
            s2_map[s2[i]]++;
            if (s1[i] != s2[i]) {
                diff++;     // Count the number of different characters
                if (diff > 2)
                    return false;
            }   
        }

        // Check if the two strings have the same characters
        for(int i = 0; i < s1.size(); i++) {
            if (s2_map[s1[i]] != s1_map[s1[i]]) {
                return false;
            }
        }   

        return true;
    }
};

int main() {
    Solution s;
    std::vector<std::pair<std::string, std::string>> testCases = {
        {"bank", "kanb"},
        {"attack", "defend"},
        {"kelb", "kelb"},
        {"abcd", "dcba"},
        {"abcd", "abdc"},
        {"aabbcc", "ccbbaa"},
        {"abc", "acb"},
        {"abc", "abc"},
        {"a", "a"},
        {"", ""}
    };

    for (const auto& testCase : testCases) {
        std::cout << "s1: " << testCase.first << ", s2: " << testCase.second << " -> " 
                  << (s.areAlmostEqual(testCase.first, testCase.second) ? "true" : "false") << std::endl;
    }

    return 0;
}