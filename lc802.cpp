#include <vector>
#include <iostream>
#include <set>
#include <stack>

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
            //std::set<int> visited;

            for(int j = 0; j < nodes.size(); j++) {
                //vector<int> stak;
                stack<int> stak;
                set<int> inStack; 

                // do DFS for each node
                stak.push(nodes[j]);
                inStack.insert(nodes[j]);
                while(stak.size() > 0) {
                    int node = stak.top();
                    stak.pop();
                    
                    vector<int> connectedNodes = graph[node];
                    for(int k = 0; k < connectedNodes.size(); k++) {
                        if (inStack.find(connectedNodes[k]) != inStack.end()) {
                            isSafe = false;
                            break;
                        }

                        inStack.insert(connectedNodes[k]);
                        stak.push(connectedNodes[k]);
                    }
                    inStack.erase(node);

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
