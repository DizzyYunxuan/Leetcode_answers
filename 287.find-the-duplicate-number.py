#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
class Solution:
    def findDuplicate(self, nums) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
✔ Accepted
  ✔ 53/53 cases passed (80 ms)
  ✔ Your runtime beats 62.26 % of python3 submissions
  ✔ Your memory usage beats 7.14 % of python3 submissions (16.2 MB)
# if __name__ == "__main__":
#     res = Solution().findDuplicate([1,3,4,2,2])

#     def findDuplicate(self, nums: List[int]) -> int:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return nums[i]
# ✔ Accepted
#   ✔ 53/53 cases passed (72 ms)
#   ✔ Your runtime beats 94.1 % of python3 submissions
#   ✔ Your memory usage beats 7.14 % of python3 submissions (16 MB)      


#     def findDuplicate(self, nums: List[int]) -> int:
#         d = {}
#         for i in nums:
#             if i in d:
#                 return i
#             else:
#                 d[i] = True
# ✔ Accepted
#   ✔ 53/53 cases passed (84 ms)
#   ✔ Your runtime beats 37.65 % of python3 submissions
#   ✔ Your memory usage beats 7.14 % of python3 submissions (16.3 MB)

