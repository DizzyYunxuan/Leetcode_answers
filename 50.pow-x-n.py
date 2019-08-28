#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1: # Check n is even or odd
                pow *= x
            x *= x
            n >>= 1
        return pow
✔ Accepted
  ✔ 304/304 cases passed (32 ms)
  ✔ Your runtime beats 92.09 % of python3 submissions
  ✔ Your memory usage beats 6.9 % of python3 submissions (13.7 MB)
# if __name__ == "__main__":
#     Solution().myPow(10., 7)

