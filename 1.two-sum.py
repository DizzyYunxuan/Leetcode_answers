#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             j = ( target - nums[i] )
#             temp = nums[i]
#             nums[i] = None
#             if j in nums:
#                 idx = nums.index(j)   
#                 return [i, idx]                
#             else:
#                 nums[i] = temp
#                 continue

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             nums[i] = [nums[i], i]
        
#         nums.sort()
#         for i in range(len(nums)):
#                 start = i+1
#                 end = len(nums) - 1
#                 mid = int((start + end)/2)
#                 while start <= end :         
#                     if nums[mid][0] + nums[i][0] == target:
#                         return [nums[i][1], nums[mid][1]]
#                     elif nums[mid][0] + nums[i][0] < target:
#                         start = mid + 1
#                     else:
#                         end = mid - 1

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        nums.sort()
        start = 0
        end = len(nums) - 1
        while True:
            if nums[start][0] + nums[end][0] > target:
                end -= 1
            elif nums[start][0] + nums[end][0] < target:
                start += 1
            else:
                return [nums[start][1], nums[end][1]]


# class Solution:
#     def twoSum(self, nums, target):
#         d = {}
#         for i, n in enumerate(nums):
#             m = target - n
#             if m in d:
#                 return [d[m], i]
#             else:
#                 d[n] = i
