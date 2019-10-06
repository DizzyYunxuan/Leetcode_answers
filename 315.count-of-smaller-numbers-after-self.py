#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class Solution:
    def countSmaller(self, nums):
        enum = list(enumerate(nums))
        res = [0] * len(nums)
        self.solver(enum, res)
        return res

    def solver(self, nums, res):
        mid = len(nums) // 2
        if not mid:
            return nums
        else:
            l, r = self.solver(nums[:mid], res), self.solver(nums[mid:], res)
            for i in range(len(nums)-1, -1, -1):
                if not r or l and l[-1][1] > r[-1][1]:
                    res[l[-1][0]] += len(r)
                    nums[i] = l.pop()
                else:
                    nums[i] = r.pop()
            return nums
Accepted
16/16 cases passed (176 ms)
Your runtime beats 51.61 % of python3 submissions
Your memory usage beats 12.5 % of python3 submissions (18.2 MB)
# if __name__ == "__main__":
#     res = Solution().countSmaller([5,2,6,1])
# @lc code=end

