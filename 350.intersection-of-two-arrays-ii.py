#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1, d2 = {}, {}
        for i in nums1:
            d1[i] = d1.get(i, 0) + 1
        
        for i in nums2:
            d2[i] = d2.get(i, 0) + 1

        res = []
        for k in d1:
            n2 = d2.get(k, -1)
            if n2 > 0: res += [k] * min(d1[k], d2[k])
        return res


 Accepted
61/61 cases passed (48 ms)
Your runtime beats 87.09 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.8 MB)       
# @lc code=end

