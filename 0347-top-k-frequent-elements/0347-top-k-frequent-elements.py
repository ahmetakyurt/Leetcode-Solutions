class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = dict()
        for number in nums:
            myDict[number] = myDict.get(number, 0) + 1
        
        ans = []
        maxCount = max(myDict.values())
        while len(ans) < k:
            for key, value in myDict.items():
                if value == maxCount:
                    ans.append(key)
                    myDict[key] = -1
            maxCount = max(myDict.values())
        return ans