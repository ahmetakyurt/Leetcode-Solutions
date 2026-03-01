class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxRepeated = 0
        nums.sort()

        i = 0
        curr = 0
        if nums == []:
            return 0
        streak = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0

            while i < len(nums) and curr == nums[i]  :
                i += 1

            streak +=1

            maxRepeated = max(maxRepeated, streak)
            curr += 1
        return maxRepeated
            
