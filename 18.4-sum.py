#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    # def fourSum(self, nums, target: int):
    #     res = []
    #     nums.sort()
    #     for i in range(len(nums) - 3):
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue
    #         for j in range(i+1, len(nums) - 2):
    #             if j > i+1 and nums[j] == nums[j-1]:
    #                 continue
    #             l, r = j + 1, len(nums) - 1
    #             while l < r:
    #                 tmp = nums[i]+nums[j]+nums[l]+nums[r]
    #                 if  tmp > target:
    #                     r -= 1
    #                 elif tmp < target:
    #                     l += 1
    #                 else:
    #                     res.append([nums[i],nums[j],nums[l],nums[r]])
    #                     while l < r and nums[l] == nums[l+1]:
    #                         l += 1
    #                     while l < r and nums[r] == nums[r-1]:
    #                         r -= 1
    #                     l += 1
    #                     r -= 1
    #     return res
# ✔ Accepted
#   ✔ 282/282 cases passed (1056 ms)
#   ✔ Your runtime beats 33.19 % of python3 submissions
#   ✔ Your memory usage beats 9.13 % of python3 submissions (13.7 MB)

    def fourSum(self, nums, target: int):
        nums.sort()
        result = []
        self.findNsum(0, len(nums)-1, 4, nums, target, [], result)
        return result

    def findNsum(self, l, r, N, nums, target, res, result):
        if N < 2 or r-l+1<2 or N*nums[r] < target or N*nums[l] > target:
            return
        if N == 2:
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    result.append(res + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        else:
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    self.findNsum(i+1, r, N-1, nums, target-nums[i], res+[nums[i]], result)
         
# ✔ Accepted
#   ✔ 282/282 cases passed (88 ms)
#   ✔ Your runtime beats 92.07 % of python3 submissions
#   ✔ Your memory usage beats 8.2 % of python3 submissions (13.5 MB)




# if __name__ == '__main__':
#     res = Solution().fourSum([0,0,0,0], 1)
#     print(res)
