#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
class Solution:
    def maxPoints(self, points) -> int:
        from collections import Counter
        all_points = Counter(tuple(point) for point in points )
        no_repeats = list(all_points.keys())
        if len(no_repeats) == 1: return all_points[no_repeats[0]]
        res = 0
        for i in range(len(no_repeats)):
            x1, y1 = no_repeats[i][0], no_repeats[i][1]
            d = {}
            for j in range(i+1, len(no_repeats)):
                x2, y2 = no_repeats[j][0], no_repeats[j][1]
                dx, dy = x1 - x2, y1 - y2
                g = self.gcd(dy, dx)
                if g != 0:
                    dy //= g
                    dx //= g
                if "{}/{}".format(dy, dx) in d:
                    d["{}/{}".format(dy, dx)] += all_points[no_repeats[j]]
                else:
                    d["{}/{}".format(dy, dx)] = all_points[no_repeats[j]]
            if d.values():
                res = max(res, max(d.values()) + all_points[no_repeats[i]])
            else:
                res = max(res, 0 + all_points[no_repeats[i]])
        return res
    def gcd(self, x, y):
            if y == 0:
                return x
            else:
                return self.gcd(y, x % y)
✔ Accepted
  ✔ 36/36 cases passed (76 ms)
  ✔ Your runtime beats 77.67 % of python3 submissions
  ✔ Your memory usage beats 42.86 % of python3 submissions (13.9 MB)
# if __name__ == "__main__":
#     res = Solution().maxPoints([[0,0],[94911151,94911150],[94911152,94911151]])
#     x = 1
