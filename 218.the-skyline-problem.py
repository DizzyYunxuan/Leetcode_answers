#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

class Solution:
    def getSkyline(self, buildings):
        if not buildings: return
        if len(buildings) == 1: return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

        mid  = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)

    def merge(self, left, right):

        res = []
        l, r, lheight, rheight = 0, 0, 0, 0
        while l < len(left) and r < len(right):
            if left[l][0] < right[r][0]:
                ct = [left[l][0], max(left[l][1], rheight)]
                lheight = left[l][1]
                l += 1
            elif left[l][0] > right[r][0]:
                ct = [right[r][0], max(right[r][1], lheight)]
                rheight = right[r][1]
                r += 1
            else:
                ct = [left[l][0], max(left[l][1], right[r][1])]
                lheight, rheight = left[l][1], right[r][1]
                l += 1
                r += 1
            if len(res) == 0 or ct[1] != res[-1][1]:
                res.append(ct)
        res += left[l:] or right[r:]
        return res
✔ Accepted
  ✔ 36/36 cases passed (168 ms)
  ✔ Your runtime beats 30.44 % of python3 submissions
  ✔ Your memory usage beats 10 % of python3 submissions (18.4 MB)

# if __name__ == "__main__":
#     buildings = [ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ]
#     res = Solution().getSkyline(buildings)
