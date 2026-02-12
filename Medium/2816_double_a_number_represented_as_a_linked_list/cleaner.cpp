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
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr) {
            ListNode* next_node = curr->next;
            curr->next = prev; 
            prev = curr;
            curr = next_node;
        }
        return prev;
    }

    ListNode* doubleIt(ListNode* head) {
        head = reverse(head);
        ListNode* curr = head;
        int carry = 0;
        while (curr) {
            int sum = carry;
            sum += (2 * curr->val);
            carry = sum / 10;
            int node_val = sum % 10;

            curr->val = node_val;
            
            if (curr->next == nullptr && carry) {
                ListNode* carry_node = new ListNode(carry);
                curr->next = carry_node;
                curr = curr->next;
            }
            curr = curr->next;
        }

        return reverse(head);
    }
};
