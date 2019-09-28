#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
✔ Accepted
  ✔ 22/22 cases passed (28 ms)
  ✔ Your runtime beats 97.83 % of python3 submissions
  ✔ Your memory usage beats 6.9 % of python3 submissions (13.7 MB)
