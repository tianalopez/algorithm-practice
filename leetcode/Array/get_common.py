# Given two integer arrays nums1 and nums2,
# sorted in non-decreasing order, return the minimum
# integer common to both arrays. If there is no common integer
# amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and
# nums2 if both arrays have at least one occurrence of that integer.

#!Difficulty: Easy
#!Category: Array


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        data = {}
        for i in range(len(nums1)):
            if nums1[i] not in data.keys():
                data[nums1[i]] = 0
        for j in range(len(nums2)):
            if nums2[j] in data.keys():
                data[nums2[j]] = 1
        maximums = [num for num in data.keys() if data[num] == 1]
        if len(maximums) >= 1:
            return min(maximums)
        else:
            return -1
