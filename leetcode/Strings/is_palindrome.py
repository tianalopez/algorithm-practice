# A phrase is a palindrome if, after converting all
# uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

#!Difficulty: Easy
#!Category: String


class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [char for char in s if char.isalnum()]
        clean_string = "".join(letters).lower()
        if clean_string == clean_string[::-1]:
            return True
        return False
