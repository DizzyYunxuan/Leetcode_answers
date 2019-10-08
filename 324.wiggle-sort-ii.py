#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2]) - 1
        # a, b, c, d = nums[0::2], nums[1::2],nums[half::-1], nums[:half:-1]
        nums[0::2], nums[1::2] = nums[half::-1], nums[:half:-1]
        # x = 1
        # return
Accepted
44/44 cases passed (184 ms)
Your runtime beats 99.27 % of python3 submissions
Your memory usage beats 11.11 % of python3 submissions (16.5 MB)
# if __name__ == "__main__":
#     res = Solution().wiggleSort([1, 5, 1, 1, 6, 4])




# @lc code=end

