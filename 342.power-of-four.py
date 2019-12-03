#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and num&(num-1) == 0 and len(bin(num)[3:]) % 2 == 0
# @lc code=end

Accepted
1060/1060 cases passed (20 ms)
Your runtime beats 99.18 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.7 MB)