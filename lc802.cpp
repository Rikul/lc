#include <vector>
#include <iostream>
#include <set>

using namespace std;

class Solution {
public:
    /*
    [[1,2],[2,3],[5],[0],[5],[],[]]

    3 -> [0]
    0
    1,2 
    2,2,3
    2,3,5      // 2 again

    [[],[0,2,3,4],[3],[4],[1],[]]

    2 -> [0,2,3,4]
    0,2,3,4
    2,3,4
    3,4,3
    4,3,4
    3,4,4
    4,4,1

    2 ->  [3]    
    3
    4
    1
    0,2,3,4
    2,3,4
    3,4,3
    4.3.1
    3,1,0,2,3,4

    */

   // NOT IMPLEMENTED
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        std::set<int> safeNodes;

        for(int i = 0; i < graph.size(); i++) {
            if (graph[i].size() == 0 || (graph[i].size() == 1 && graph[i][0] == i)) { 
                    safeNodes.insert(i);
                    continue;
            }
        }

        for(int i = 0; i < graph.size(); i++) {
            std::set<int> visited;

            vector<int> q = graph[i];
            bool isSafe = true;
            while (q.size() > 0) {
                int node = q.front();
                q.erase(q.begin());
                
                if (safeNodes.find(node) != safeNodes.end()) {
                    continue;
                }   

                // its empty or points to self.
                if (graph[node].size() == 0) {
                    safeNodes.insert(node);
                    continue;
                }
            
                if (visited.find(node) != visited.end()) {
                    cout << "Cycle detected at " << node << endl;
                    isSafe = false;
                    break;
                }
                
                visited.insert(node);
                q.insert(q.end(), graph[node].begin(), graph[node].end());
            }

            if (isSafe) {
                safeNodes.insert(i);
            }
        }


        return vector<int>(safeNodes.begin(), safeNodes.end());
    }
};