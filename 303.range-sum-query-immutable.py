#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums):
        self.nums = [0]
        for i in range(len(nums)):
            self.nums.append(self.nums[-1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j+1] - self.nums[i]
Accepted
16/16 cases passed (96 ms)
Your runtime beats 55.99 % of python3 submissions
Your memory usage beats 10 % of python3 submissions (17.4 MB)
# if __name__ == "__main__":
#     obj = NumArray([-2, 0, 3, -5, 2, -1])
#     param_1 = obj.sumRange(0,2)
#     print(param_1)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

