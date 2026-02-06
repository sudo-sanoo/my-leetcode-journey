# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if not head or not head.next:
            return head.val

        res = 0
        while head:
            # shift the bit to the left by 1
            # then use OR for adding up the current bit
            res = (res << 1) | head.val
            head = head.next
        return res
