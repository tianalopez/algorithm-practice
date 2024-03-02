# Given two strings needle and haystack,
# return the index of the first occurrence of needle
# in haystack, or -1 if needle is not part of haystack.

#!Difficulty: Easy
#!Type: String


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
