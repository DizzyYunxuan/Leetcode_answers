#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums):
        self.nums = nums
        # self.nums = [0]
        # for n in nums:
        #     self.nums.append(self.nums[-1] + n)
        

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val
        # cur = self.nums[i+1] - self.nums[i]
        # delta = val - cur
        # self.nums[i+1:] = list(map(lambda x: x+delta, self.nums[i+1:]))
        # print(self.nums)

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])


Accepted
10/10 cases passed (832 ms)
Your runtime beats 5.2 % of python3 submissions
Your memory usage beats 33.33 % of python3 submissions (17 MB)
        # return self.nums[j+1]-self.nums[i]
# if __name__ == "__main__":
#     nums = [1, 3, 5]
#     obj = NumArray(nums)

#     param_2 = obj.sumRange(0,2)
#     obj.update(1,2)
#     param_3 = obj.sumRange(0,2)
#     print(param_3)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end

