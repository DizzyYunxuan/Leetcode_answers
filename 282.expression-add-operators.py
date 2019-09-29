#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#
class Solution:
    def addOperators(self, num: str, target: int):
        res = []
        for i in range(1, len(num)+1):
            if i > 1 and num[0] == '0':
                continue
            self.solver(num[i:], target, num[:i], int(num[:i]), int(num[:i]), res)
        return res

    def solver(self, num, target, path, total, pre, res):
        if not num:
            if total == target:
                res.append(path)
            return
        for i in range(1, len(num)+1):
            cur = num[:i]
            if i > 1 and num[0] == '0':
                continue
            self.solver(num[i:], target, path+'+'+cur, total+int(cur), int(cur), res)
            self.solver(num[i:], target, path+'-'+cur, total-int(cur), -int(cur), res)
            self.solver(num[i:], target, path+'*'+cur, total-pre+int(cur)*pre, pre*int(cur), res)
✔ Accepted
  ✔ 20/20 cases passed (956 ms)
  ✔ Your runtime beats 34.2 % of python3 submissions
  ✔ Your memory usage beats 33.33 % of python3 submissions (14.1 MB) 
# if __name__ == "__main__":
#     res = Solution().addOperators("105", 5)


