#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        max_num, res = 0, 0
        for i in d:
            if d[i] > max_num:
                max_num = d[i]
                res = i
        return res
✔ Accepted
  ✔ 44/44 cases passed (200 ms)
  ✔ Your runtime beats 51.83 % of python3 submissions
  ✔ Your memory usage beats 7.14 % of python3 submissions (15.3 MB)

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
✔ Accepted
  ✔ 44/44 cases passed (180 ms)
  ✔ Your runtime beats 99.47 % of python3 submissions
  ✔ Your memory usage beats 7.14 % of python3 submissions (15.3 MB)      
