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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // O(n) runtime, O(1) memory
        if (head->next == nullptr) {
            head = head->next;
            return head;
        }

        ListNode* slow = head;
        ListNode* fast = head;

        for (int i=1; i<=n; i++) {
            fast = fast->next;
        }

        if (!fast) {
            head = head->next;
            return head;
        }

        while (fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }

        slow->next = slow->next->next;

        return head;
        
        // // O(n) runtime, O(n) memory
        // std::unordered_map<int, ListNode*> node_map;

        // int i = 1;
        // ListNode* node = head;
        // while (node) {
        //     node_map[i-1] = node;
        //     if (node->next == nullptr) {
        //         int idx = i-n-1;
        //         if (node_map.count(idx)) {
        //             node = node_map[idx];
        //             node->next = node->next->next;
        //             break;
        //         }
        //         else { // always idx = -1 to end up in this else clause, meaning to remove the first node
        //             head = head->next;
        //             return head;
        //         }
        //     }
        //     node = node->next;
        //     i++;
        // }
        
        // return head;
    }
};
