#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int):
        if num == 0:
            return [0]
        res = [0, 1]
        pw = 0
        for i in range(2, num+1):
            if i == 2 ** (pw + 1):
                pw += 1
                res.append(1)
                continue
            res.append(1+res[i-2**pw])
        return res

Accepted
15/15 cases passed (108 ms)
Your runtime beats 35.62 % of python3 submissions
Your memory usage beats 5 % of python3 submissions (19.7 MB)

# if __name__ == "__main__":
#     res = Solution().countBits(2)
#     print(res)
# @lc code=end

