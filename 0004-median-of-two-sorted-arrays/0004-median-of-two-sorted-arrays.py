class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        
        # Binary search'ü her zaman kısa olan dizi (nums2) üzerinde yapıyoruz
        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        lo, hi = 0, n2 * 2
        while lo <= hi:
            mid2 = (lo + hi) // 2
            mid1 = n1 + n2 - mid2
            
            # (mid-1)//2 formülü sanal indekslerden gerçek indekslere geçişi sağlar
            l1 = float('-inf') if mid1 == 0 else nums1[(mid1 - 1) // 2]
            l2 = float('-inf') if mid2 == 0 else nums2[(mid2 - 1) // 2]
            
            r1 = float('inf') if mid1 == n1 * 2 else nums1[mid1 // 2]
            r2 = float('inf') if mid2 == n2 * 2 else nums2[mid2 // 2]
            
            if l1 > r2:
                # nums1'in sol tarafı çok büyük, mid1'i küçültmek için mid2'yi büyüt
                lo = mid2 + 1
            elif l2 > r1:
                # nums2'in sol tarafı çok büyük, mid2'yi küçült
                hi = mid2 - 1
            else:
                # Doğru kesim noktasındayız
                return (max(l1, l2) + min(r1, r2)) / 2.0
        
        return -1.0