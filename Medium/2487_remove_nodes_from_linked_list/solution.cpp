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
    ListNode* removeNodes(ListNode* head) {
        // Intuition:
        // 1. Reverse the linked list
        // 2. Traverse the linked list, keep track of the max(curr->val)
        // 3. Delete every node when curr->val < max(curr->val)
        // 4. Do not delete the node when curr->val > max(curr->val), then update the curr->val
        // 5. Repeat 2-4 until curr == nullptr
        // 6. Reverse the linked list again

        // Step 1
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }
        head = prev;
        
        // Step 2
        int max_val = head->val;
        curr = head;
        while (curr != nullptr) {
            while (curr->next != nullptr && (curr->next->val < max_val)) {
                // Step 3
                curr->next = curr->next->next;
            }
            if (curr->next == nullptr) {
                break;
            }
            // Step 4
            max_val = curr->next->val;
            curr = curr->next;
        }

        // Step 6
        prev = nullptr;
        curr = head;
        while (curr != nullptr) {
            ListNode* next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node; 
        }
        head = prev;

        return head;
    }
};
