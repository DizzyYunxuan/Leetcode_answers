#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#
import itertools
class Solution:
    
    def isScramble(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        if sorted(s1) != sorted(s2):
            return False
        if l1 < 4 or s1 == s2:
            return True
        for i in range(1, l1):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
    ✔ Accepted
  ✔ 283/283 cases passed (40 ms)
  ✔ Your runtime beats 96.84 % of python3 submissions
  ✔ Your memory usage beats 33.33 % of python3 submissions (13.9 MB)
if __name__ == "__main__":
    res = Solution().isScramble('abb', 'bab')
