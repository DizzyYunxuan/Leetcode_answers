#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    # def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]
#     ✔ Accepted
#   ✔ 294/294 cases passed (32 ms)
#   ✔ Your runtime beats 97.88 % of python3 submissions
#   ✔ Your memory usage beats 5.41 % of python3 submissions (13.8 MB)
    def addBinary(self, a: str, b: str) -> str:
        la, lb = len(a), len(b)
        if la >= lb:
            b = '0' * (la - lb) + b
        else:
            a = '0' * (lb - la) + a
        i, carry, res = -1, 0, ''       
        while i >= -max(la, lb):
            t = int(a[i]) + int(b[i]) + carry
            cur, carry = t % 2, t // 2
            res = str(cur) + res
            i -= 1
        if carry:
            res = '1' + res
        return res
✔ Accepted
  ✔ 294/294 cases passed (48 ms)
  ✔ Your runtime beats 18.24 % of python3 submissions
  ✔ Your memory usage beats 5.41 % of python3 submissions (13.9 MB)
