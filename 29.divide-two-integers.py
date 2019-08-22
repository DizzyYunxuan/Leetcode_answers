#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
#   ✔ Accepted
#   ✔ 989/989 cases passed (32 ms)
#   ✔ Your runtime beats 97.03 % of python3 submissions
#   ✔ Your memory usage beats 7.41 % of python3 submissions (13.9 MB)
# if __name__ == '__main__':
#     res = Solution().divide(-2147483648,-1)
#     print(res)
