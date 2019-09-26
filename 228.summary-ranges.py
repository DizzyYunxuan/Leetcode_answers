#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return [str(nums[0])]
        res = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if i - start > 1:
                    res.append(str(nums[start])+'->'+str(nums[i-1]))
                else:
                    res.append(str(nums[start]))
                start = i
        if nums[-1] - nums[-2] == 1:
            res.append(str(nums[start])+'->'+str(nums[-1]))
        else:
            res.append(str(nums[-1]))
        return res
✔ Accepted
  ✔ 28/28 cases passed (32 ms)
  ✔ Your runtime beats 90.15 % of python3 submissions
  ✔ Your memory usage beats 16.67 % of python3 submissions (14 MB)

# if __name__ == "__main__":
#     res = Solution().summaryRanges([0,2,3,4,6,8,9])
