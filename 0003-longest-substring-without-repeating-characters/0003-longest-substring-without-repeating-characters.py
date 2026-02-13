class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentWindow = ""
        maxLength = 0
        for char in s:
            
            if char in currentWindow:
                currentWindow = currentWindow[currentWindow.index(char) +1:]

            currentWindow += char
            print(currentWindow)

            maxLength = max(maxLength, len(currentWindow))

        return maxLength

            

            
