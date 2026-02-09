class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        myList = list(mySet)
        return len(myList) != len(nums)
        