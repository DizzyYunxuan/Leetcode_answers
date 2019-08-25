#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0
        res = 0
        lmax, rmax = [height[0]], [height[len(height) - 1]]
        for i in range(1, len(height)):
            lmax.append(max(lmax[i-1], height[i]))
        for j in range(len(height)-2, -1, -1):
            rmax.insert(0, max(rmax[0], height[j]))
        for i in range(1, len(height)-1):
            res += min(lmax[i], rmax[i]) - height[i]

        return res

# if __name__ == '__main__':
#     res = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
#     print(res)
