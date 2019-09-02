#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x < (mid + 1)* (mid + 1):
                return mid
            elif x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1
    # def mySqrt(self, x):
    #     l, r = 0, x
    #     while l <= r:
    #         mid = l + (r-l)//2
    #         if mid * mid <= x < (mid+1)*(mid+1):
    #             return mid
    #         elif x < mid * mid:
    #             r = mid
    #         else:
    #             l = mid + 1
✔ Accepted
  ✔ 1017/1017 cases passed (40 ms)
  ✔ Your runtime beats 80.63 % of python3 submissions
  ✔ Your memory usage beats 6.45 % of python3 submissions (13.9 MB)

        