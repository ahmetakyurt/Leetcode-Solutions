class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)

        if len(nums) <2:
            return []

        prefixList = [0] * len(nums)
        prefixList[0] = nums[0]
        suffixList = [0] * len(nums)
        suffixList[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefixList[i] = prefixList[i-1] * nums[i]
        for i in range(len(nums)-2, -1, -1):
            suffixList[i] = suffixList[i+1] * nums[i]    
        
        print(prefixList, suffixList)
        myList = [0] * len(nums)
        myList[0] = suffixList[1]
        myList[-1] = prefixList[-2]
        for i in range(1, len(nums)-1):
            myList[i] = prefixList[i-1] * suffixList[i+1]

        return myList
            