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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (head == nullptr && head->next == nullptr) return head;

        int node_val = 0;
        ListNode* prev = head;
        ListNode* curr = head->next;
        while (curr != nullptr) {
            node_val = gcd(prev->val, curr->val);
            ListNode* node = new ListNode(node_val, prev->next);
            prev->next = node;

            prev = curr;
            curr = curr->next;
        }

        return head;
    }
};
