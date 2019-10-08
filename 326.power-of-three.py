#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return False
        while not n % 3:
            n //= 3
        return n == 1
Accepted
21038/21038 cases passed (88 ms)
Your runtime beats 71.39 % of python3 submissions
Your memory usage beats 7.41 % of python3 submissions (14 MB)

# @lc code=end

