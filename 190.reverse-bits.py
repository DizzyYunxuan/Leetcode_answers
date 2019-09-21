#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]
        if len(s) < 32:
            s = (32-len(s))*'0' + s
        s = s[::-1]
        return int(s, 2)
✔ Accepted
  ✔ 600/600 cases passed (20 ms)
  ✔ Your runtime beats 57.39 % of python submissions
  ✔ Your memory usage beats 92.86 % of python submissions (11.6 MB)
# if __name__ == "__main__":
#     res = Solution().reverseBits(43261596)
