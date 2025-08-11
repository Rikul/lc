#include <vector>

using namespace std;


class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool carry = false;

        for(int i = digits.size() - 1; i >= 0; i--) {
            
            if (digits[i] == 9) {
                carry = true;
                digits[i] = 0;
            } else {
                digits[i] += 1;
                carry = false;
            }

            if (! carry)
                break;
        }

        if (carry) {
            digits.insert(digits.begin(), 1);
        }

        return digits;

    }

};