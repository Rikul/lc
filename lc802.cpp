#include <vector>
#include <iostream>
#include <set>

using namespace std;

class Solution {
public:
    
   // NOT IMPLEMENTED
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        std::set<int> safeNodes;

        // loop through each node
        for(int i = 0; i < graph.size(); i++) {
            bool isSafe = true;

            // no edges
            if (graph[i].size() == 0) {  
                safeNodes.insert(i);
                continue;
            }
            
            // check each connected node
            vector<int> nodes = graph[i];
            std::set<int> visited;

            for(int j = 0; j < nodes.size(); j++) {
                vector<int> q;

                // do BFS for each node
                q.push_back(nodes[j]);
                visited.clear();
                visited.insert(i);

                while (q.size() > 0) {
                    int n = q.front();
                    q.erase(q.begin());

                    if (safeNodes.find(n) != safeNodes.end()) {
                       continue;
                    }

                    // its empty
                    if (graph[n].size() == 0) {
                        safeNodes.insert(n);
                        continue;
                    }

                    if (visited.find(n) != visited.end()) {
                        //cout << "Cycle detected at " << n << " : " << "i: " << i << " j: " << j << endl;
                        isSafe = false;
                        break;
                    }

                    visited.insert(n);
                    q.insert(q.end(), graph[n].begin(), graph[n].end());
                }
            }

            if (isSafe) {
                safeNodes.insert(i);
            }
        }


        return vector<int>(safeNodes.begin(), safeNodes.end());
    }
};


int main() {
    Solution s;

    // Example 1: Graph with a cycle
    vector<vector<int>> graph1 = {{1,2},{2,3},{5},{0},{5},{},{}};
    vector<int> result1 = s.eventualSafeNodes(graph1);
    cout << "Safe nodes in graph1: ";
    for(int i = 0; i < result1.size(); i++) {
        cout << result1[i] << " ";
    }
    cout << endl;

    // Example 2: Graph with no cycles
    vector<vector<int>> graph2 = {{1,2},{2,3},{3},{4},{},{}};
    vector<int> result2 = s.eventualSafeNodes(graph2);
    cout << "Safe nodes in graph2: ";
    for(int i = 0; i < result2.size(); i++) {
        cout << result2[i] << " ";
    }
    cout << endl;

    // Example 3: Graph with a self-loop
    vector<vector<int>> graph3 = {{1},{2},{0},{3}};
    vector<int> result3 = s.eventualSafeNodes(graph3);
    cout << "Safe nodes in graph3: ";
    for(int i = 0; i < result3.size(); i++) {
        cout << result3[i] << " ";
    }
    cout << endl;

    // Example 4: Graph with multiple cycles
    vector<vector<int>> graph4 = {{1},{2},{0,3},{4},{5},{3}};
    vector<int> result4 = s.eventualSafeNodes(graph4);
    cout << "Safe nodes in graph4: ";
    for(int i = 0; i < result4.size(); i++) {
        cout << result4[i] << " ";
    }
    cout << endl;

    return 0;
}
