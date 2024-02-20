# take a string and number of rows, if put in a zigzag pattern with the given number of rows
# what is the new string returned

#!Difficulty: Medium


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s

        rows = [[] for row in range(numRows)]
        index = 0
        step = 1
        for character in s:
            rows[index].append(character)

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        for i in range(numRows):
            rows[i] = "".join(rows[i])
        return "".join(rows)
