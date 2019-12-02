#
# @lc app=leetcode id=335 lang=python3
#
# [335] Self Crossing
#

# @lc code=start
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False

Accepted
29/29 cases passed (32 ms)
Your runtime beats 93.83 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (13.7 MB)
# @lc code=end

