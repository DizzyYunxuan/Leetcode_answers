#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
class Solution:
    def calculate(self, s: str) -> int:
        pre, cur, nxt = 0, 0, 0
        sign = '+'
        for i in s:
            if i.isdigit():
                nxt = nxt*10 + int(i)
            elif i.isspace():
                continue
            else:
                if sign == '+':
                    pre += cur
                    cur = nxt
                elif sign == '-':
                    pre += cur
                    cur = -nxt
                elif sign == '*':
                    cur *= nxt
                else:
                    if cur < 0:
                        cur = -(-cur // nxt)
                    else:
                        cur //= nxt
                nxt = 0
                sign = i
        if sign == '+':
            pre += cur
            cur = nxt
        elif sign == '-':
            pre += cur
            cur = -nxt
        elif sign == '*':
            cur *= nxt
        else:
            if cur < 0:
                cur = -(-cur // nxt)
            else:
                cur //= nxt
        nxt = 0
        sign = i
        return pre + cur
✔ Accepted
  ✔ 109/109 cases passed (104 ms)
  ✔ Your runtime beats 69.97 % of python3 submissions
  ✔ Your memory usage beats 22.22 % of python3 submissions (15.1 MB)

# if __name__ == "__main__":
#     res = Solution().calculate("1*2-3/4+5*6-7*8+9/10")       

                


