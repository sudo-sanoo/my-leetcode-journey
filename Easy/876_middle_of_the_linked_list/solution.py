# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edgecase handling, if head is null or only one node exists, return head immediately
        if not head or not head.next:
            return head
        
        # create a reference that point to the first node
        # Visualization:
        #             slow, fast
        #                 |  
        #                 V
        #       head ---> 1 -> 2 -> 3 -> 4 -> 5
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # the output will be the entire head, if you do:
        #
        #   slow = head
        #       return slow
        #
        # Why?
        # In a linked list, a node is the start of a chain.
        # When you return a node, you are returning this node and everything after it
        #
        # Analogy:
        # Think of a train with 6 cars connected in a line.
        # Each car is linked to the next one.
        #
        # If you return the 1st car (head),
        # you get the entire train.
        #
        # If you return the 3rd car,
        # you get the train starting from the 3rd car
        # until the last one.
        #
        # In a linked list, returning a node returns
        # that node and everything after it.
