#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp < 0:
                    l += 1
                elif tmp > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
#      ✔ Accepted
#       ✔ 313/313 cases passed (868 ms)
#       ✔ Your runtime beats 72.14 % of python3 submissions
#       ✔ Your memory usage beats 54.79 % of python3 submissions (16.8 MB)
# if __name__ == '__main__':
#     res = Solution().threeSum([-1,0,1,2,-1,-4])
#     print(res)
