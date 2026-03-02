class Solution:
    def isPalindrome(self, s: str) -> bool:
        charList = list(s)
        myList = [char.lower() for char in charList if char.isalnum()] 
        if myList == myList[::-1]:
            return True
        return False

        """
        isalpha
        isdigit
        isspace
        islower
        isdecimal
        """