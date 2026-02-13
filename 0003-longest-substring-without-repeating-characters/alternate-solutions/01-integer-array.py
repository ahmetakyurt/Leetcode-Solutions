class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        You can think of charIndexes list as an hasmap of all ascii characters. There is total of 128 ascii characters.
        Ord(char) -> returns ascii code of the character E.g "a": 097.
        We store current char's last seen index in the hasmap.
        If current char's previous index is in between current index of the char and left part of the current window
        """
        charIndexes = [-1] * 128
        left = 0
        maxLength =0

        for index, char in enumerate(s):
            # If last identical char is found in current window
            if (charIndexes[ord(char)]) >= left:
                left = charIndexes[ord(char)] + 1
            
            charIndexes[ord(char)] = index

            maxLength = max(maxLength, index - left + 1)
    
        return maxLength
