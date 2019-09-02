#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp, pe = path.split('/'), []
        for i in tmp:
            if i and i != '.' and i != '..':
                pe.append(i)
            elif i == '..' and pe:
                pe.pop()     
        return '/' + '/'.join(pe)
✔ Accepted
  ✔ 254/254 cases passed (40 ms)
  ✔ Your runtime beats 62.21 % of python3 submissions
  ✔ Your memory usage beats 14.29 % of python3 submissions (13.8 MB)
# if __name__ == "__main__":
#     res = Solution().simplifyPath("/a//b////c/d//././/..")
#     x = 1



