class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = list(s)

        if len(s) != len(t):
            return False
            
        for letter in t:
            if letter in letters:
                letters.remove(letter)

            else:
                return False

        return True

        