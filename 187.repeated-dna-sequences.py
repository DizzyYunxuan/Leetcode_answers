#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d, n, i, res = {}, len(s), 0, []
        while i < n - 9:
            if s[i:i+10] not in d:
                d[s[i:i+10]] = 1
            else:
                d[s[i:i+10]] += 1
            i += 1
        
        for seq in d:
            if d[seq] >= 2:
                res.append(seq)
        return res
✔ Accepted
  ✔ 32/32 cases passed (76 ms)
  ✔ Your runtime beats 49.84 % of python3 submissions
  ✔ Your memory usage beats 16.67 % of python3 submissions (27.2 MB)
