#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:

    vector<int> prms(int left, int right) {

        int n = right;
        vector<bool> is_prime(n+1, true);
        is_prime[0] = is_prime[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (is_prime[i]) {
                for (int j = i * i; j <= n; j += i)
                    is_prime[j] = false;
            }
        }

        vector<int> result;
        for(int n = left; n <= right && result.size() < 2; n++) {
            if (is_prime[n])
                result.push_back(n);
        }

        if (result.size() < 2)
            return {-1,-1};

        return result;

    }

};

int main() {
    Solution s;
    vector<int> res = s.prms(100, 200);

    //cout << s.closestPrimes(10, 20) << endl;
    return 0;
}