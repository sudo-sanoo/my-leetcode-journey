# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # NOTES:
        # 1. initialize pointers to 2 consecutive nodes
        # 2. find value of the node to be inserted
        #    x_val = gcd(18, 6) = 6
        # 3. construct the node
        #    'x' is a node with: x.val = 6 and x.val = null (for now)
        # 4. update the new inserted node's reference to point to the original node after prev
        #    now both x.next and prev.next point to curr
        # 5. update prev's reference to point to node 'x'
        #    now our head looks like this (following example 1)
        #     (head)  (prev)    (curr)
        #        V      V          V
        #       18  ->  6 (x)  ->  6  ->  10  ->  3  
        # 6. update prev's and curr's reference for the next insertion
        #    now our head looks like this (following example 1)
        #     (head)            (prev)  (curr)
        #        V                 V      V
        #       18  ->  6 (x)  ->  6  ->  10  ->  3  

        # edgecase check
        if not head or not head.next:
            return head
        
        # 1
        prev = head
        curr = head.next
        while curr: # use curr to avoid gcd(prev.val, null)
            x_val = gcd(prev.val, curr.val) # 2
            x = ListNode(x_val)             # 3
            x.next = prev.next              # 4
            prev.next = x                   # 5
            
            # 6
            prev = curr # prev = x.next works as well, bc x.next = curr. But prev = next is more readable
            curr = curr.next

        return head
