#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, bars):
        if not bars or len(bars) < 3:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume
#     ✔ Accepted
#   ✔ 315/315 cases passed (60 ms)
#   ✔ Your runtime beats 73.8 % of python3 submissions
#   ✔ Your memory usage beats 6.98 % of python3 submissions (14.5 MB)
    
    # def trap(self, height) -> int:
    #     if not height or len(height) < 3:
    #         return 0
    #     res = 0
    #     lmax, rmax = [height[0]], [height[len(height) - 1]]
    #     for i in range(1, len(height)):
    #         lmax.append(max(lmax[i-1], height[i]))
    #     for j in range(len(height)-2, -1, -1):
    #         rmax.insert(0, max(rmax[0], height[j]))
    #     for i in range(1, len(height)-1):
    #         res += min(lmax[i], rmax[i]) - height[i]

    #     return res

# if __name__ == '__main__':
#     res = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
#     print(res)
