#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, -1
        while i < len(s):
            if not '0'<= s[i] <= '9' and not 'a' <= s[i] <= 'z':
                i += 1
            elif not '0'<= s[j] <= '9' and not 'a' <= s[j] <= 'z':
                j -= 1               
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
✔ Accepted
  ✔ 476/476 cases passed (88 ms)
  ✔ Your runtime beats 6.94 % of python3 submissions
  ✔ Your memory usage beats 46.43 % of python3 submissions (14.3 MB)
# if __name__ == "__main__":
#     res = Solution().isPalindrome("race a car")
    

