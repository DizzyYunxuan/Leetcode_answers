#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i, j = 0, len(x) - 1
        while i < j and x[i] == x[j]:
            i += 1
            j -= 1
        return False if i < j else True
    # ✔ Accepted
    #     ✔ 11509/11509 cases passed (68 ms)
    #     ✔ Your runtime beats 80.83 % of python3 submissions
    #     ✔ Your memory usage beats 47.71 % of python3 submissions (13.3 MB)
