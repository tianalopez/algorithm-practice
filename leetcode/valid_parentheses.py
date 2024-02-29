# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

#!Difficulty: Easy


class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if char in mappings.values():
                stack.append(char)
            elif char in mappings.keys():
                if not stack or stack.pop() != mappings[char]:
                    return False

        return not stack
