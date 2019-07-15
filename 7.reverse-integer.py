#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        L = [i for i in s[1:]]
        L.reverse()
        if s[0] != '-':
            res = int(''.join(L)+s[0])
            return 0 if res > 2**31-1 or res < -2**31 else res
        else:
            res = int(s[0]+ ''.join(L))
            return 0 if res > 2**31-1 or res < -2**31 else res
    # ✔ Accepted
    #     ✔ 1032/1032 cases passed (32 ms)
    #     ✔ Your runtime beats 93.91 % of python3 submissions
    #     ✔ Your memory usage beats 31.3 % of python3 submissions (13.3 MB)


