#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        curPlace = 10
        while curPlace <= n:
            curPlace *= 10
        curPlace //= 10
        res = 0
        nxtn = n % curPlace
        res += self.countDigitOne(nxtn)
        return res + (n // curPlace) * self.cal(curPlace) + (curPlace if (n//curPlace) != 1 else nxtn+1)

    def cal(self, n):
        if n == 10:
            return 1
        return 10 * self.cal(n // 10) + n // 10\
✔ Accepted
  ✔ 40/40 cases passed (32 ms)
  ✔ Your runtime beats 89.84 % of python3 submissions
  ✔ Your memory usage beats 100 % of python3 submissions (13.8 MB)


# if __name__ == "__main__":
#     res = Solution().countDigitOne(10)
#     print(res)
