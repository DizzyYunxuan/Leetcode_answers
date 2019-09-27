#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
class Solution:
    def productExceptSelf(self, nums):
        res = [0] * len(nums)
        order, reverseorder = [nums[0]], [nums[-1]]
        for i in range(1, len(nums)):
            order.append(order[-1]*nums[i])
        for i in range(len(nums)-2, -1, -1):
            reverseorder.append(reverseorder[-1]*nums[i])
        res[0], res[-1] = reverseorder[-2], order[-2]
        for i in range(1, len(nums)-1):
            res[i] = order[i-1] * reverseorder[len(nums) - i - 2]
        return res
✔ Accepted
  ✔ 17/17 cases passed (152 ms)
  ✔ Your runtime beats 19.38 % of python3 submissions
  ✔ Your memory usage beats 84 % of python3 submissions (20.4 MB)

# if __name__ == "__main__":
#     res = Solution().productExceptSelf([1,2,3,4])
