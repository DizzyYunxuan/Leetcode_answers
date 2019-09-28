#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        return (0 + n)* (n + 1)//2 - sum(nums)
✔ Accepted
  ✔ 122/122 cases passed (176 ms)
  ✔ Your runtime beats 16.5 % of python3 submissions
  ✔ Your memory usage beats 6.45 % of python3 submissions (14.9 MB)



#     def missingNumber(self, nums) -> int:
#         xor, n = 0, len(nums)
#         for i in nums:
#             xor ^= i
#         for i in range(n+1):
#             xor ^= i
#         return xor
# ✔ Accepted
#   ✔ 122/122 cases passed (180 ms)
#   ✔ Your runtime beats 12.04 % of python3 submissions
#   ✔ Your memory usage beats 6.45 % of python3 submissions (15 MB)
# if __name__ == "__main__":
#     res = Solution().missingNumber([3,0,1])
#     print(res)

