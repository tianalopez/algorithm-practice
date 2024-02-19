# Given a string s, find the length of the longest
# substring without repeating characters.

#!Difficulty: Medium


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = {}
        left = 0
        length = 0
        for right in range(len(s)):
            character = s[right]
            if character in substrings and substrings[character] >= left:
                left = substrings[character] + 1
            else:
                length = max(length, right - left + 1)
            substrings[character] = right

        return length
