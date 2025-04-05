#include <string>
#include <algorithm>
using namespace std;

class Solution {
    public:
        int minimumRecolors(string blocks, int k) {
            
            int min_ops = 100;
            for(int i=0; i < blocks.length() - k + 1; i++) {
                int w = 0;
                for (int j=i; j < i+k; j++) {
                    if (blocks[j] == 'W') 
                        w++;
    
                    if (w > min_ops)
                        break;
                }
    
                min_ops = min(w, min_ops);
            }
    
            return min_ops;
        }
    };