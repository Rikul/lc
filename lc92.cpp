#include <vector>
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* node = head;
        ListNode* leftnode = NULL;
        std::vector<int> stack;

        for(int i=1; i<=right; i++) {
            if (left == i) {
                leftnode = node;
            }    

            if (left <= i && i <= right) {
                stack.push_back(node->val);
            }

            node = node->next;
        }

        while(leftnode && !stack.empty()) {
            int v = stack.back();
            stack.pop_back();
            leftnode->val = v;
            leftnode = leftnode->next;
        }


        return head;   
    }
};


int main() {
    Solution s;
    ListNode * node = s.reverseBetween(new ListNode(1, new ListNode(2, new ListNode(3, NULL))),1,2);
    while(node) {
        std::cout << node->val << " ";
        node = node->next;
    }
    std::cout << std::endl;
}