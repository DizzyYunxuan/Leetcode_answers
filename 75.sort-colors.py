#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums)-1)
    def quicksort(self, nums, start, end):
        if start >= end:
            return
        pivot = nums[start]
        i, j = start, end
        while i < j:
            while i < j and nums[j] > pivot:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] < pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = pivot
        self.quicksort(nums, start, i-1)
        self.quicksort(nums, i+1, end)
 ✔ Accepted
  ✔ 87/87 cases passed (40 ms)
  ✔ Your runtime beats 67.65 % of python3 submissions
  ✔ Your memory usage beats 6.25 % of python3 submissions (13.6 MB)       
# if __name__ == "__main__":
    # nums = [3,1,4,2,7]
    # res = Solution().quicksort(nums, 0, 4)


