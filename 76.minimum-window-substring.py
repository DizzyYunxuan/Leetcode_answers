#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
✔ Accepted
  ✔ 268/268 cases passed (152 ms)
  ✔ Your runtime beats 41.7 % of python3 submissions
  ✔ Your memory usage beats 5.55 % of python3 submissions (14.5 MB)
            
# if __name__ == "__main__":
#     s, t = 'ADOBECODEBANC', 'ABC'
#     # s, t = 'bba', 'ab'
#     res = Solution().minWindow(s, t)       
#     print(res)


