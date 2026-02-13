class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndexes = [-1] * 128
        left = 0
        maxLength = 1 if len(s) == 1 else 0

        for index, char in enumerate(s):
            if (charIndexes[ord(char)]) >= left:
                left = charIndexes[ord(char)] + 1
            
            charIndexes[ord(char)] = index

            maxLength = max(maxLength, index - left + 1)
    
        return maxLength



            

            
