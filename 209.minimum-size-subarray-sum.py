#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums:
            return 0
        start, end, curs = 0, 0, nums[0]
        shortest = float('inf')
        flag = False
        while end < len(nums):
            if curs < s:
                end += 1
                if end == len(nums):
                    break
                curs += nums[end]
            else:
                flag = True
                shortest = min(shortest, end - start + 1)
                curs -= nums[start]
                start += 1
        return shortest if flag else 0

✔ Accepted
  ✔ 15/15 cases passed (96 ms)
  ✔ Your runtime beats 24.25 % of python3 submissions
  ✔ Your memory usage beats 7.69 % of python3 submissions (16.4 MB)
# if __name__ == "__main__":
#     res = Solution().minSubArrayLen(3, [1,1])
