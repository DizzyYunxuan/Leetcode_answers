#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.split()
        if len(s) == 0:
            return 0
        s = s[0]
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        ss = ''
        for i in range(1, len(s)):
            if s[i] in nums:
                ss += s[i]
            else:
                break
        ss = s[0] + ss
        try:
            res = int(float(ss))
            if res > 2**31 - 1 or res < -2**31:
                raise OverflowError
        except OverflowError:
            if ss[0] == '-':
                return -2**31
            else:
                return 2**31 - 1
        except ValueError:
            return 0
        
        return res    
      
    # ✔ Accepted
    #     ✔ 1079/1079 cases passed (40 ms)
    #     ✔ Your runtime beats 80.89 % of python3 submissions
    #     ✔ Your memory usage beats 77.4 % of python3 submissions (13.2 MB)

