#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        res = []
        # self.quicksort(intervals, 0, len(intervals)-1)
        # intervals.sort()
        left, right = [], []
        for i in intervals:
            if i[1] < newInterval[0]:
                left += [i]
            elif i[0] > newInterval[1]:
                right += [i]
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        if left:
            res += left
        res += [newInterval]
        if right:
            res += right
        return res

    def quicksort(self, nums, start, end):
        if start < end:
            piovt = nums[start]
            left, right = start, end
            while left < right:
                while left < right and nums[right][0] > piovt[0]:
                    right -= 1
                if left < right:
                    nums[left][0] = nums[right][0]
                    left += 1
                while left < right and nums[left][0] < piovt[0]:
                    left += 1
                if left < right:
                    nums[right][0] = nums[left][0]
                    right -= 1
            nums[left][0] = piovt[0]
            self.quicksort(nums, start, left-1)
            self.quicksort(nums, left+1, end)
✔ Accepted
  ✔ 154/154 cases passed (88 ms)
  ✔ Your runtime beats 91.22 % of python3 submissions
  ✔ Your memory usage beats 8 % of python3 submissions (17 MB)
# if __name__ == "__main__":
#     res = Solution().insert([[2,5],[6,7],[8,9]], [0,1])
#     print(res)
