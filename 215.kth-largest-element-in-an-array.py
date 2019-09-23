#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return self.quicksort(nums, 0, len(nums)-1, k)

    def quicksort(self, nums, low, high, k):
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            if low < high:
                nums[low] = nums[high]
            while low < high and nums[low] < pivot:
                low += 1
            if low < high:
                nums[high] = nums[low]
        nums[low] = pivot

        if low == len(nums) - k:
            return nums[low]
        elif low < len(nums) - k:
            return self.quicksort(nums, low+1, len(nums)-1, k)
        else:
            return self.quicksort(nums, 0, low-1, k)
#  ✔ Accepted
#   ✔ 32/32 cases passed (1872 ms)
#   ✔ Your runtime beats 11.39 % of python3 submissions
#   ✔ Your memory usage beats 5 % of python3 submissions (19.7 MB)           


    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     import heapq
    #     return heapq.nlargest(k, nums)[-1]
# ✔ Accepted
#   ✔ 32/32 cases passed (76 ms)
#   ✔ Your runtime beats 80.61 % of python3 submissions
#   ✔ Your memory usage beats 10 % of python3 submissions (14.7 MB)
