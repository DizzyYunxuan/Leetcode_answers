#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.Tree = [0] * self.n + nums
        for i in range(self.n-1, 0, -1):
            self.Tree[i] = self.Tree[2*i] + self.Tree[2*i+1]
  
    def update(self, i: int, val: int) -> None:
        pos = i + self.n
        self.Tree[pos] = val
        while pos > 0:
            l, r = pos, pos
            if pos % 2 == 0:
                r += 1
            else:
                l -= 1
            self.Tree[pos//2] = self.Tree[l] + self.Tree[r]
            pos //= 2
    def sumRange(self, i: int, j: int) -> int:
        l, r = i + self.n, j + self.n
        s = 0
        while l <= r:
            if l % 2 == 1:
                s += self.Tree[l]
                l += 1
            if r % 2 == 0:
                s += self.Tree[r]
                r -= 1
            l, r = l // 2 , r // 2
        return s
Accepted
10/10 cases passed (168 ms)
Your runtime beats 68.91 % of python3 submissions
Your memory usage beats 33.33 % of python3 submissions (17.6 MB)
# if __name__ == "__main__":
#     nums = [1, 3, 5]
#     obj = NumArray(nums)

#     param_2 = obj.sumRange(0,2)
#     obj.update(1,2)
#     param_3 = obj.sumRange(0,2)
#     print(param_2)
#     print(param_3)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end

