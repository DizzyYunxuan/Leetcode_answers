#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        # self.quiksort(nums, 0, len(nums)-1)
        self.getAllp(nums, [], res)
        return res
    def getAllp(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.getAllp(nums[:i]+nums[i+1:], path+[nums[i]], res)
    
    def quiksort(self,nums, start, end):
        if start < end:
            piovt = nums[start]
            left, right = start, end
            while left < right:
                while left < right and nums[right] > piovt:
                    right -= 1
                if left < right:
                    nums[left] = nums[right]
                    left += 1
                while left < right and nums[left] < piovt:
                    left += 1
                if left < right:
                    nums[right] = nums[left]
                    right -= 1
            nums[left] = piovt
            self.quiksort(nums, start, left-1)
            self.quiksort(nums, left+1, end)


# ✔ Accepted
#   ✔ 30/30 cases passed (52 ms)
#   ✔ Your runtime beats 99.55 % of python3 submissions
#   ✔ Your memory usage beats 11.11 % of python3 submissions (13.8 MB)
# if __name__ == "__main__":
#     res = Solution().permuteUnique([5,4,8,1,6])
