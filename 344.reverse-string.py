#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < len(s) // 2:
            s[i], s[~i] = s[~i], s[i]
            i += 1

Accepted
478/478 cases passed (216 ms)
Your runtime beats 88.41 % of python3 submissions
Your memory usage beats 98.84 % of python3 submissions (17.2 MB)
# @lc code=end

