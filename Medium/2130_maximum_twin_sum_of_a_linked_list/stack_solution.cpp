/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        std::stack<int> st;
        int res = 0;
        
        ListNode* slow = head;
        ListNode* fast = head;
        while (slow) {
            if (!fast) {
                res = max(res, st.top() + slow->val);
                st.pop();
            }
            else {
                st.push(slow->val);
            }

            slow = slow->next;
            if (fast) fast = fast->next->next;
        }
        return res;
    }
};
