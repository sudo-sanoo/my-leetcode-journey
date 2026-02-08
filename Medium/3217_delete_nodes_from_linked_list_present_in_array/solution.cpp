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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        std::unordered_set<int> st(nums.begin(), nums.end());

        // remove any beginning node thats in nums
        while (head && st.count(head->val)) {
            head = head->next;
        }

        // remove nodes after the beginning til the end thats in nums
        ListNode* curr = head;
        while (curr != nullptr) {
            while (curr->next != nullptr && st.count(curr->next->val)) {
                curr->next = curr->next->next;
            }
            curr = curr->next;
        }

        return head;
    }
};
