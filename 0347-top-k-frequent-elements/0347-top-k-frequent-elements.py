class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for num in nums:
            myDict[num] = 1 + myDict.get(num, 0)

        bucket = [[] for i in range(len(nums) +1 )]

        print(myDict)
        for num, count in myDict.items():
            bucket[count].append(num)

        ans = []
        for node in range(len(bucket) - 1, 0, -1):
            for number in bucket[node]:
                ans.append(number)

                if len(ans) == k:
                    return ans