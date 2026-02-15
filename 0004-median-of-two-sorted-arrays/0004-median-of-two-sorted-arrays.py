import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        sortedList = list()
        left = 0
        right = n

        while nums2 and nums1:
            if nums1[0] < nums2[0]:
                sortedList.append(nums1.pop(0))
            else:
                sortedList.append(nums2.pop(0))

        sortedList.extend(nums1)
        sortedList.extend(nums2)
        sum = n+m
        print(sortedList)
        if (n+m) % 2 == 0:
            return (sortedList[sum//2-1] + sortedList[sum//2])/2
        return sortedList[sum//2]