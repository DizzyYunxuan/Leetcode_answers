#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        queue = []
        res = []
        for i in range(len(nums)):
            if queue and i - queue[0] + 1 > k:
                queue.pop(0)
            while  queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i - k + 1 >= 0:
                res.append(nums[queue[0]])
        return res
✔ Accepted
  ✔ 18/18 cases passed (184 ms)
  ✔ Your runtime beats 61.21 % of python3 submissions
  ✔ Your memory usage beats 7.69 % of python3 submissions (20.1 MB)
# if __name__ == "__main__":
#     res = Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)


    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if not nums:return
    #     res = []
    #     for i in range(len(nums)-k+1):
    #         res.append(max(nums[i:i+k]))
    #     return res

