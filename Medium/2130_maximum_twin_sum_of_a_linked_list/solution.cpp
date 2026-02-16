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
        std::vector<int> st;
        int n = 0;
        while (head) {
            st.push_back(head->val);
            head = head->next;
            n++;
        }

        int l = 0;
        int r = n-1;
        int res = 0;
        while (l<r) {
            res = max(res, st[l] + st[r]);
            l++;
            r--;
        }

        return res;
    }
};
