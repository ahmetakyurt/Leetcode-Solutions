# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeList = list()
        while head:
            if head in nodeList:
                return True

            nodeList.append(head)
            head = head.next
        return False

            
           