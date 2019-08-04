#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        dis = float('inf')
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp < target:
                    l += 1
                    if abs(tmp - target) < dis:
                        res = tmp
                        dis = abs(tmp - target)
                elif tmp > target:
                    r -= 1
                    if abs(tmp - target) < dis:
                        res = tmp
                        dis = abs(tmp - target)
                else:
                    return target
        return res

#     ✔ Accepted
#   ✔ 125/125 cases passed (104 ms)
#   ✔ Your runtime beats 87.12 % of python3 submissions
#   ✔ Your memory usage beats 5.16 % of python3 submissions (13.8 MB)
# if __name__ == '__main__':
#     res = Solution().threeSumClosest([-1,2,1,-4], 1)
#     print(res)
