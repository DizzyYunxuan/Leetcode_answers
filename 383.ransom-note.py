#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m  = Counter(ransomNote), Counter(magazine)
        for k, v in r.items():
            b = m.get(k, -1)
            if b < v: return False
        return True
Accepted
129/129 cases passed (44 ms)
Your runtime beats 83.15 % of python3 submissions
Your memory usage beats 68.35 % of python3 submissions (13.9 MB)

# @lc code=end

