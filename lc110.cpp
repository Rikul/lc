/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */


#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    bool h_balanced = true;

    int height(TreeNode* root) {
        if (! h_balanced) 
            return 0;

        if (root == NULL)
            return 0;
        else {
            int h_left = height(root->left);
            int h_right = height(root->right);
            if (abs(h_left - h_right) > 1) {
                h_balanced = false;
            }
            return max(h_left, h_right) + 1;
        }
    }

public:
    bool isBalanced(TreeNode* root) {
        cout << height(root) << endl;
        return h_balanced;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    Solution sol;
    cout << sol.isBalanced(root) << endl;

    return 0;
}