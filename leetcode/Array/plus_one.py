# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

#!Difficulty: Easy
#!Category: Array


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed = digits[::-1]

        for i in range(len(reversed)):
            if reversed[i] < 9:
                reversed[i] += 1
                break
            if reversed[i] >= 9:
                reversed[i] = 0
                if i + 1 < len(reversed):
                    reversed[i + 1] = reversed[i + 1] + 1
                    if reversed[i + 1] <= 9:
                        break
                else:
                    reversed.append(1)
        return reversed[::-1]
