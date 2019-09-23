#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        maxi = 0
        for i in range(2, length+1):
            if s[:i] == s[:i][::-1]:
                maxi = max(maxi, i)
        if maxi:
            res = s[maxi:][::-1] + s
        else:
            res = s[maxi+1:][::-1] + s
        return res
✔ Accepted
  ✔ 120/120 cases passed (708 ms)
  ✔ Your runtime beats 12.91 % of python3 submissions
  ✔ Your memory usage beats 14.29 % of python3 submissions (14.2 MB)
# if __name__ == "__main__":
#     res = Solution().shortestPalindrome("aacecaaa")
