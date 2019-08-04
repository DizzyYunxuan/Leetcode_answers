#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums, target: int):
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    tmp = nums[i]+nums[j]+nums[l]+nums[r]
                    if  tmp > target:
                        r -= 1
                    elif tmp < target:
                        l += 1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res

# if __name__ == '__main__':
#     res = Solution().fourSum([0,0,0,0], 0)
#     print(res)
