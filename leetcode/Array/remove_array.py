# Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place.
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.

#!Difficulty: Easy
#!Category: Array


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for item in nums:
            if item == val:
                nums.remove(val)
        return len(nums)
