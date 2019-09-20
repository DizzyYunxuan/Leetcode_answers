#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        p_int, p_dec = numerator // denominator, numerator/denominator - numerator//denominator
        res.append(str(p_int))   
        if p_dec == 0:
            return ''.join(res)
        res.append('.')
        currest = numerator % denominator
        res_num = {currest:len(res)}
        while currest:
            currest *= 10
            cur, currest = currest // denominator, currest % denominator
            res.append(str(cur))
            if currest in res_num:
                res.insert(res_num[currest], '(')
                res.append(')')
                break
            res_num[currest] = len(res)
        return ''.join(res)
✔ Accepted
  ✔ 37/37 cases passed (32 ms)
  ✔ Your runtime beats 92.67 % of python3 submissions
  ✔ Your memory usage beats 16.67 % of python3 submissions (14 MB)

# if __name__ == "__main__":
#     numerator, denominator = -2147483648, 1
#     res = Solution().fractionToDecimal(numerator, denominator)
#     x = 1
