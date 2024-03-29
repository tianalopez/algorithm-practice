# Given an integer array nums sorted in non-decreasing order, remove
# the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted,
# you need to do the following things:

# Change the array nums such that the first k elements of nums contain
# the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

#!Difficulty: Easy
#!Category: Array


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                nums.pop(i)  # Remove the duplicate element
            else:
                i += 1  # Move to the next element only if it's not a duplicate
        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        for j in range(len(nums)):
            if nums[j] not in seen:
                seen.add(nums[j])
                nums[i] = nums[j]
                i += 1
        return i
