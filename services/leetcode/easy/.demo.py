class Solution:
    def isPalindrome(self, s: str) -> bool:

        a = ""

        for char in s:
            if  char.isalnum():
                a += char.lower()
