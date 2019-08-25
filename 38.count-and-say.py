#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            t = self.countAndSay(n-1)
            count, res, cur = 0, '', t[0]
            for i in range(len(t)):
                if t[i] != cur:
                    res += str(count) + cur
                    cur, count = t[i], 1
                else:
                    count += 1
            res += str(count) + cur
            return res

✔ Accepted
  ✔ 18/18 cases passed (32 ms)
  ✔ Your runtime beats 98.71 % of python3 submissions
  ✔ Your memory usage beats 6.38 % of python3 submissions (13.8 MB)
# if __name__ == '__main__':
#     res = Solution().countAndSay(5)
#     print(res)


