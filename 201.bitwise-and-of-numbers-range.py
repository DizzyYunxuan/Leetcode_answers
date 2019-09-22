#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        bm, bn = bin(m)[2:], bin(n)[2:]
        bm = (len(bn)-len(bm)) * '0'+bm
        i = 0
        while i < len(bm) and bm[i] == bn[i]:
            i += 1
        return int(bm[:i] + (len(bm)-i)*'0', 2)
✔ Accepted
  ✔ 8266/8266 cases passed (68 ms)
  ✔ Your runtime beats 70.18 % of python3 submissions
  ✔ Your memory usage beats 100 % of python3 submissions (14.1 MB)
# if __name__ == "__main__":
#     res = Solution().rangeBitwiseAnd(1,2)
#     print(res)
