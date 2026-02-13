# time complexity: O(N)
# space complexity: O(Min(N,M))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0 
        maxLength = 0
        charSet = set()

        for index, char in enumerate(s):
            if char in charSet:
                while char in charSet:
                    charSet.remove(s[left])
                    left+=1
                    
                charSet.add(char)
            else:
                charSet.add(char)
                maxLength = max(maxLength, index-left+1)
