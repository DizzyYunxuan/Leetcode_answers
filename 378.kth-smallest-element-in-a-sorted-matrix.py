#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        heap = []
        # if not matrix or not matrix[0]: return
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = -matrix[i][j]
                if len(heap) < k:
                    heapq.heappush(heap, val)
                elif val > heap[0]:
                    heapq.heappushpop(heap, val)
        return -heap[0]

Accepted
85/85 cases passed (204 ms)
Your runtime beats 72.64 % of python3 submissions
Your memory usage beats 9.09 % of python3 submissions (18.5 MB)


# @lc code=end

