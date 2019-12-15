#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0; right = num
        while left <= right:
            mid = (left+right)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right = mid-1
            else:
                left = mid+1
        return False
Accepted
68/68 cases passed (24 ms)
Your runtime beats 95.53 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.6 MB)


#     def isPerfectSquare(self, num: int) -> bool:
#         if num == 0 or num == 1: return True
#         i = num
#         while i**2 > num:
#             i //= 2
#         while i ** 2 <= num:
#             if i**2 == num:
#                 return True
#             i += 1
#         return False
# Accepted
# 68/68 cases passed (40 ms)
# Your runtime beats 34.51 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=end

