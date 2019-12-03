#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return 3**a
        if b == 1:
            return 3 ** (a-1) * 4
        if b == 2:
            return 3 ** a * 2


Accepted
50/50 cases passed (20 ms)
Your runtime beats 99.39 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

