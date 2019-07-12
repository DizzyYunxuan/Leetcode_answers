#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (26.70%)
# Likes:    4560
# Dislikes: 640
# Total Accepted:    460.4K
# Total Submissions: 1.7M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1 = len(nums1)
        l2 = len(nums2)      
        i, j, nums3= 0, 0, []
        mid = (l1 + l2) // 2 
        while i < l1 and j < l2 and len(nums3) != mid + 1:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if i < l1:
            while len(nums3) != mid + 1:
                nums3.append(nums1[i])
                i += 1

        elif j < l2:
            while len(nums3) != mid + 1:
                nums3.append(nums2[j])
                j += 1

        if (l1 + l2) % 2 == 0:
            return (nums3[-1] + nums3[-2]) / 2
        else:
            return nums3[-1] * 1.0
            


