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
    ListNode* doubleIt(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr) {
            ListNode* next_node = curr->next;
            curr->next = prev; 
            prev = curr;
            curr = next_node;
        }

        ListNode* dummy = new ListNode(0, prev);
        int carry = 0;
        while (prev) {
            int sum = carry;
            sum += (2 * prev->val);
            carry = sum / 10;
            int node_val = sum % 10;

            prev->val = node_val;
            
            if (prev->next == nullptr && carry) {
                ListNode* carry_node = new ListNode(carry);
                prev->next = carry_node;
                prev = prev->next;
            }
            prev = prev->next;
        }

        prev = nullptr;
        curr = dummy->next;
        while (curr) {
            ListNode* next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }

        return prev;
    }
};
