class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        sortedList = list()
        left = 0
        right = n


        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                sortedList.append(nums1[p1])
                p1 += 1
            else:
                sortedList.append(nums2[p2])
                p2 += 1

        sortedList.extend(nums1[p1:])
        sortedList.extend(nums2[p2:])
        sum = n+m
        print(sortedList)
        if (n+m) % 2 == 0:
            return (sortedList[sum//2-1] + sortedList[sum//2])/2
        return sortedList[sum//2]