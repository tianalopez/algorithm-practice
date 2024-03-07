# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the
# index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

#!Difficulty: Easy
#!Category: Array


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            if nums[i] < target and (i + 1) > len(nums) - 1:
                return i + 1
            if nums[i] < target and nums[i + 1] >= target:
                return i + 1
            elif nums[i] < target and nums[i + 1] < target:
                i += 1
