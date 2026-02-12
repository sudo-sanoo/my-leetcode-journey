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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        std::stack<int> l1_stack;
        std::stack<int> l2_stack;

        ListNode* l1_curr = l1;
        ListNode* l2_curr = l2;

        while (l1_curr || l2_curr) {
            if (l1_curr) {
                l1_stack.push(l1_curr->val);
                l1_curr = l1_curr->next;
            }
            if (l2_curr) {
                l2_stack.push(l2_curr->val);
                l2_curr = l2_curr->next;
            }
        }

        ListNode* dummy = new ListNode(0);
        int carry = 0;
        while (!l1_stack.empty() || !l2_stack.empty()) {
            int node_val = carry;
            if (!l1_stack.empty()) {
                node_val += l1_stack.top();
                l1_stack.pop();
            }
            if (!l2_stack.empty()) {
                node_val += l2_stack.top();
                l2_stack.pop();
            }
            carry = node_val / 10;
            node_val = node_val % 10; 

            ListNode* new_node = new ListNode(node_val);

            new_node->next = dummy->next;
            dummy->next = new_node;
        }

        if (carry) {
            ListNode* new_node = new ListNode(carry);
            new_node->next = dummy->next;
            dummy->next = new_node;
        }

        return dummy->next;
    }
};
