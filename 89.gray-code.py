#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
class Solution:
    def grayCode(self, n: int):
        res = [0]
        for i in range(1, 2**n):
            res.append(res[-1] ^ (i & -i))
        return res
 ✔ Accepted
  ✔ 12/12 cases passed (36 ms)
  ✔ Your runtime beats 88.16 % of python3 submissions
  ✔ Your memory usage beats 5.26 % of python3 submissions (13.6 MB)       


# if __name__ == "__main__":
#     res = Solution().grayCode(3)
