# Given a string s, return the longest palindromic substring in s

#!Difficulty: Medium


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def left_right(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        answer = ""
        for i in range(len(s)):
            first_sub = left_right(i, i)

            if len(first_sub) > len(answer):
                answer = first_sub

            sec_sub = left_right(i, i + 1)
            if len(sec_sub) > len(answer):
                answer = sec_sub
        return answer
