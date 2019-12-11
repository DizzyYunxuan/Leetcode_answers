#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        leadingZeroRes = 0
        for i in range(1, n):
            leadingZeroRes += i*self.A(9, i-1)
        return self.A(10, n) + leadingZeroRes
    
    def A(self, bot, up):
        if up == 0: return 1
        res = 1
        for i in range(bot, bot-up, -1):
            res *= i
        return res
Accepted
9/9 cases passed (28 ms)
Your runtime beats 89.16 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.6 MB)

# @lc code=end

