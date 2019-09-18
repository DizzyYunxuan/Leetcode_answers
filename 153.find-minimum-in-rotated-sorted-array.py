#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
class Solution:
    def findMin(self, nums) -> int:
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]     
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid - 1
✔ Accepted
  ✔ 146/146 cases passed (44 ms)
  ✔ Your runtime beats 91.44 % of python3 submissions
  ✔ Your memory usage beats 6 % of python3 submissions (13.8 MB)
# if __name__ == "__main__":
#     nums = [4,5,6,7,8,9,0,1,2,3]
#     res = Solution().findMin(nums)
            
