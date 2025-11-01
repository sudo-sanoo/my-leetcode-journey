# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 2:
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        dummy = ListNode(0, head)

        prev = dummy
        while prev.next:
            if prev.next.val in nums:
                prev.next = prev.next.next
            else:
                prev = prev.next

        return dummy.next

# # Solution 1:
# class Solution(object):
#     def modifiedList(self, nums, head):
#         """
#         :type nums: List[int]
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         nums = set(nums)
#         dummy = ListNode(0, head)

#         prev = dummy
#         curr = head
#         while curr:
#             if curr.val in nums:
#                 prev.next = curr.next
#             else:
#                 prev = prev.next

#             curr = curr.next

#         return dummy.next
