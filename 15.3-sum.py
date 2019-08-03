#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums):
        i, res = 0, []
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                k = j + 1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i],nums[j],nums[k]]
                        tmp.sort()
                        if tmp not in res:
                            res.append(tmp)
                    k += 1
                j += 1
            i += 1
        return res

# if __name__ == '__main__':
#     res = Solution().threeSum([-1,0,1,2,-1,-4])
#     print(res)
