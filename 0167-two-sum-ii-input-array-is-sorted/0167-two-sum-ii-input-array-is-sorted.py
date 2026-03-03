class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            missing = target-nums[i]
            left = i+1
            right = len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == missing:
                    return [i+1, mid+1]
                elif nums[mid] < missing:
                    left = mid+1
                else:
                    right = mid-1