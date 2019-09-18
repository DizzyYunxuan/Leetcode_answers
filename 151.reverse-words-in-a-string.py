#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(s.strip().split()[::-1])
# ✔ Accepted
#   ✔ 25/25 cases passed (32 ms)
#   ✔ Your runtime beats 93.99 % of python3 submissions
#   ✔ Your memory usage beats 8.7 % of python3 submissions (14.5 MB)

    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        l, i = [], 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return ""
        else:
            s = s[i:]
        j = len(s) - 1
        while s[j] == ' ':
            j -= 1
        s = s[:j+1]
        i, start = 0, 0
        while i < len(s):
            if s[i] == ' ':
                l.append(s[start:i])          
                while s[i] == ' ':
                    i += 1
                start = i
                continue
            i += 1
        l.append(s[start:])
        l = l[::-1]
        return ' '.join(l)
✔ Accepted
  ✔ 25/25 cases passed (52 ms)
  ✔ Your runtime beats 15.39 % of python3 submissions
  ✔ Your memory usage beats 8.7 % of python3 submissions (14.4 MB)
# if __name__ == "__main__":
#     a = "  hello world!  "
#     res = Solution().reverseWords(a)
#     x = 1

