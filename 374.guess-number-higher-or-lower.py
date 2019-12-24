#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 0, n
        mid = (low + high) // 2
        while guess(mid):
            if guess(mid) < 0:
                high = mid - 1
            elif guess(mid) > 0:
                low = mid + 1
            mid = (low + high) // 2
        return mid
Accepted
25/25 cases passed (24 ms)
Your runtime beats 82.09 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=end

