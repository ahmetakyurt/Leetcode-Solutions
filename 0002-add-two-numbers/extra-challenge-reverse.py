# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    This challenge version returns reversed LinkedList of the normal expected one
    """
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        excess = 0
        while l1 or l2 or excess:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1 + n2 + excess
            excess = total //10
            total = total %10

            curr.next = ListNode(total)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        dummy = dummy.next
        return self.reverse(dummy)

