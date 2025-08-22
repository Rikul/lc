#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next = nullptr;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:

    ListNode* reverse_nodes(ListNode* first, ListNode* last) {
        if (! first || ! last) 
            return nullptr;

        //ListNode *node = first;
        ListNode *second = first->next;

        while (second != nullptr && second != last) {
            ListNode *third = second->next;
            second->next = first;
            first = second;
            second = third;
        }

        first->next = last;
        return first; 
    
    }


    void reverse_node(ListNode* left_of_start, ListNode* start, ListNode* end, ListNode* right_of_end) {

        if (! start) 
            return;
                
        vector<int> values;
        ListNode*node = start;
        while (node != right_of_end) {
            values.push_back(node->val);
            node = node->next;
        }

        int i = values.size() - 1;
        node = start;
        while (i >= 0 && node != right_of_end) {
            node->val = values[i--];
            node = node->next;
        }

    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* left_of_start = NULL;
        ListNode* node = head;
        
        if (k <= 1) 
            return head;

        while(node != NULL) {
            ListNode* start = node;
            ListNode* end, *right_of_end;

            for(int i=1; i<k; i++) {
                if (! node) 
                    break;
                node = node->next;
            }
            
            if (! node) {
                break;
            }
            
            end = node;
            right_of_end = end->next;
            reverse_node(left_of_start, start, end, right_of_end);
            left_of_start = end;
            node = right_of_end;
        }    

        while(head) {
            cout << head->val << " ";
            head = head->next;
        }
        cout << endl;


        return NULL;
    }
};

int main() {
    ListNode* head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
    int k = 2;
    Solution sol;
    sol.reverseKGroup(head, k); 
    
}
