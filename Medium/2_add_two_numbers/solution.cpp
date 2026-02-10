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
        // add l1 and l2 nodes respectively
        // l1 and l2 nodes reversed is the value
        // then return the result

        // implement a queue to store up to a googol
        std::queue<int> q;
        int carry = 0;
        while (l1 && l2) {
            int total = l1->val + l2->val + carry;
            carry = 0;
            if (total >= 10) {
                total -= 10;
                carry++;
            }
            q.push(total);
            
            l1 = l1->next;
            l2 = l2->next;
        }

        // this while loop runs if l1 is longer than l2
        while (l1) {
            int total = l1->val + carry;
            carry = 0;
            if (total >= 10) {
                total -= 10;
                carry++;
            }
            q.push(total);

            l1 = l1->next;
        }

        // this while loop runs if l2 is longer than l1
        while (l2) {
            int total = l2->val + carry;
            carry = 0;
            if (total >= 10) {
                total -= 10;
                carry++;
            }
            q.push(total);

            l2 = l2->next;
        }

        // if theres still a carry push it to the q
        if (carry) q.push(carry);

        // transform the queue to a linked list
        ListNode* head = new ListNode(q.front());
        q.pop();
        ListNode* curr = head;
        while (!q.empty()) {
            int q_val = q.front();
            q.pop();

            ListNode* new_node = new ListNode(q_val);
            curr->next = new_node;
            curr = new_node;
        }

        return head;
    }
};
