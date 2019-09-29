#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        p_word = set(zip(pattern, words))
        return len(words) == len(pattern) and len(p_word) == len(set(pattern)) == len(set(words))       
   ✔ Accepted
  ✔ 33/33 cases passed (28 ms)
  ✔ Your runtime beats 97.9 % of python3 submissions
  ✔ Your memory usage beats 5.55 % of python3 submissions (13.6 MB)     
# if __name__ == "__main__":
#     res = Solution().wordPattern('abba', 'dog cat cat fish')

