#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
class Solution:
    def grayCode(self, n: int):
        s, res = '0' * n, [0]
        for i in range(len(s)):
            if s[i] == '0':
                s = s[:i]+'1'+s[i+1:]
                res.append(int(s, base=2))
        for i in range(len(s)-1):
            if s[i] == '1':
                s = s[:i]+'0'+s[i+1:]
                res.append(int(s, base=2))
        return res


# if __name__ == "__main__":
#     pass
