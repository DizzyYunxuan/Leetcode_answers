#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1
            ,'V': 5
            ,'X': 10
            ,'L': 50
            ,'C': 100
            ,'D': 500
            ,'M': 1000
        }
        s = s.replace('CD', 'CCCC', -1)
        s = s.replace('CM', 'DCCCC', -1)
        s = s.replace('XL', 'XXXX', -1)
        s = s.replace('XC', 'LXXXX', -1)
        s = s.replace('IV', 'IIII', -1)
        s = s.replace('IX', 'VIIII', -1)
        res = 0
        for i in s:
            res += dic[i]
        return res 

#         ✔ Accepted
#   ✔ 3999/3999 cases passed (52 ms)
#   ✔ Your runtime beats 78.5 % of python3 submissions
#   ✔ Your memory usage beats 5.03 % of python3 submissions (13.9 MB)
