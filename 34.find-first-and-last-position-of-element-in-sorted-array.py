#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums, target: int):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                start, end = mid, mid
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1
                return [start+1, end-1]
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]

# ✔ Accepted
#   ✔ 88/88 cases passed (100 ms)
#   ✔ Your runtime beats 74.77 % of python3 submissions
#   ✔ Your memory usage beats 5.36 % of python3 submissions (15 MB)

    def searchRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]: left = mid + 1
                else: right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]: left = mid + 1
                else: right = mid - 1
            return right
            
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
# ✔ Accepted
#   ✔ 88/88 cases passed (96 ms)
#   ✔ Your runtime beats 92.32 % of python3 submissions
#   ✔ Your memory usage beats 5.36 % of python3 submissions (14.8 MB)

