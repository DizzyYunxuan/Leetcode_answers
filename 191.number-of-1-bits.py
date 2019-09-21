#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]
        res = 0
        for i in s:
            if i == '1':
                res += 1
        return res
✔ Accepted
  ✔ 601/601 cases passed (12 ms)
  ✔ Your runtime beats 93.16 % of python submissions
  ✔ Your memory usage beats 100 % of python submissions (11.6 MB)
