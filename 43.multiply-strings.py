#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res= (len(num1) + len(num2)) * [0]
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                mr = int(num1[i]) * int(num2[j])
                pos = j - len(num2) + 1 + i -len(num1)
                res[pos] += mr
                carry, res[pos] = res[pos] // 10, res[pos] % 10
                res[pos-1] += carry
        res = ''.join(map(str, res))
        return '0' if not res.lstrip('0') else res.lstrip('0')
# if __name__ == '__main__':
#     res = Solution().multiply('0', '0')

