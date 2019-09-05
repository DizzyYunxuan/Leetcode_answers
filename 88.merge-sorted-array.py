#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        i, j = 0, 0
        for k in range(m, -1, -1):
            if nums1[k] != 0:
                k += 1
                break
            
        while j < n:
            if nums2[j] <= nums1[i]:
                tail = k
                k += 1
                while tail >= i:
                    nums1[tail] = nums1[tail-1]
                    tail -= 1
                m += 1
                nums1[i] = nums2[j]
                j += 1
            elif i > m - 1:
                nums1[i] = nums2[j]
                j += 1
            i += 1
✔ Accepted
  ✔ 59/59 cases passed (44 ms)
  ✔ Your runtime beats 72.12 % of python3 submissions
  ✔ Your memory usage beats 6.15 % of python3 submissions (14 MB)

# if __name__ == "__main__":
#     nums1 = [-1,0,0,3,3,3,0,0,0]
#     nums2 = [1,2,2]
#     res = Solution().merge(nums1, 6,nums2,3)

