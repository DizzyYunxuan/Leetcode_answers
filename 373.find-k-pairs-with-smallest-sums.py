#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j] , i, j])
        push(0, 0)
        res = []
        while queue and len(res) < k:
            _, i, j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, j)
        return res

Accepted
27/27 cases passed (48 ms)
Your runtime beats 90.62 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.8 MB)

      2   4   6
   +------------
 1 |  3   5   7
 7 |  9  11  13
11 | 13  15  17


    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         from itertools import product
#         res = sorted(product(nums1, nums2), key=sum)
#         return res[:k]
# Accepted
# 27/27 cases passed (196 ms)
# Your runtime beats 33.71 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (41.7 MB)
# @lc code=end

