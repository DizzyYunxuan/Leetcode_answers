#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
class Solution:
    def combinationSum3(self, k: int, n: int):
        self.res = []
        self.solver(k, n, [], 0)
        return self.res

    def solver(self, k, n, path, idx):
        if n == 0 and k == 0:
            self.res.append(path)
            return
        if n < 0:
            return
        for i in range(idx+1, 10):
            self.solver(k-1, n-i, path+[i], i)
✔ Accepted
  ✔ 18/18 cases passed (32 ms)
  ✔ Your runtime beats 95.72 % of python3 submissions
  ✔ Your memory usage beats 11.11 % of python3 submissions (13.8 MB)
# if __name__ == "__main__":
#     res = Solution().combinationSum3(3, 7)
