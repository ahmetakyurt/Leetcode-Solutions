class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = dict()
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in myDict:
                myDict[sortedString].append(string)
            else:
                myDict[sortedString] = [string]

        return [liste for liste in myDict.values()]