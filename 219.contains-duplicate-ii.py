#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                for idx in d[nums[i]]:
                    if abs(idx - i) <= k:
                        return True
                d[nums[i]] += [i]
            else:
                d[nums[i]] = [i]
        return False
✔ Accepted
  ✔ 23/23 cases passed (108 ms)
  ✔ Your runtime beats 70.15 % of python3 submissions
  ✔ Your memory usage beats 12.5 % of python3 submissions (24.8 MB)
