class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow = head
        fast = head
        
        # fast.next kontrolü önemli, çünkü fast ikişer ikişer atlıyor!
        while fast and fast.next:
            slow = slow.next          # 1 adım
            fast = fast.next.next     # 2 adım
            
            if slow == fast:          # Bellekte aynı adreste buluştular!
                return True
                
        return False