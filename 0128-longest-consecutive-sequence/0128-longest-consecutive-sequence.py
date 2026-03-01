class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        mySet2 = mySet.copy()
    
        maxRepeated = 1
        if nums == []:
            return 0
        for num in mySet2:
            repeated = 1
            if num-1 in mySet:
                continue

            while num+1 in mySet:
                repeated += 1
                num = num+1
                maxRepeated = max(maxRepeated, repeated)
                mySet.remove(num)
        return maxRepeated
            
