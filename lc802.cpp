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
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<int> safeNodes;

        for(int i = 0; i < graph.size(); i++) {
            if (graph[i].size() == 0) { 
                safeNodes.push_back(i);
                continue;
            }

            vector<int> nodes = graph[i];

        }


        return vector<int>();
    }
};