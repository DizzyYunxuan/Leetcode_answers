#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
class Solution:
    def titleToNumber(self, s: str) -> int:
        i, res, exp = len(s) - 1, 0, 0
        while i >= 0:
            cur = ord(s[i])
            res += (cur - 64) * 26 ** exp 
            exp += 1
            i -= 1
        return res
✔ Accepted
  ✔ 1000/1000 cases passed (40 ms)
  ✔ Your runtime beats 58.16 % of python3 submissions
  ✔ Your memory usage beats 9.09 % of python3 submissions (14 MB)

# if __name__ == "__main__":
#     res = Solution().titleToNumber('ZY')
