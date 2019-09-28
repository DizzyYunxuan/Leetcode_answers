#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        while num // 10 != 0:
            t, tsum = num, 0
            while t != 0:
                tsum += t % 10
                t //= 10
            num = tsum
        return tsum
✔ Accepted
  ✔ 1101/1101 cases passed (40 ms)
  ✔ Your runtime beats 59.41 % of python3 submissions
  ✔ Your memory usage beats 5.26 % of python3 submissions (13.9 MB)
