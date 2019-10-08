#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        res = []
        for i in range(k+1):
            if i <= len(nums1) and k-i <= len(nums2):
                c1, c2 = self.getMaxdigits(nums1, i), self.getMaxdigits(nums2, k-i)
                res = max(res, self.mergeAndGetMaxres(c1, c2))
        return res

    def getMaxdigits(self, nums, k):
        drop = len(nums) - k
        out = []
        for n in nums:
            while drop and out and out[-1] < n:
                drop -= 1
                out.pop()
            out.append(n)
        return out[:k]

    def mergeAndGetMaxres(self, nums1, nums2):
        return [max(nums1, nums2).pop(0) for _ in nums1+nums2]

Accepted
102/102 cases passed (364 ms)
Your runtime beats 77.91 % of python3 submissions
Your memory usage beats 20 % of python3 submissions (13.9 MB)


# if __name__ == "__main__":
#     nums1 = [3,4,6,5]
#     nums2 = [9,1,2,5,8,3]
#     # res = Solution().getMaxdigits(nums2, 3)
#     res = Solution().maxNumber(nums1, nums2, 5)
#     print(res)




######################TLE#######################
    # def maxNumber(self, nums1, nums2, k: int):
    #     l1, l2 = len(nums1), len(nums2)
    #     p1, p2 = [], []

    #     for k1 in range(-min(0, l2-k), min(l1, k)+1):
    #         p1.append(self.getMaxdigits(nums1, k1, 0, [])[1])
    #         p2.append(self.getMaxdigits(nums2, k-k1, 0, [])[1])
        
    #     path = []
    #     for i in range(len(p1)):
    #         tp = self.mergeAndGetMaxres(p1[i], p2[i])
    #         path = max(path, tp)
    #     return path


    # def getMaxdigits(self, nums, l, cursum, path):
    #     if not nums or not l:
    #         return cursum, path
    #     res, respath = 0, []
    #     for i in range(len(nums)):
    #         ts, tp = self.getMaxdigits(nums[i+1:], l-1, cursum*10+nums[i], path+[nums[i]])
    #         if ts > res:
    #             res, respath = ts, tp
    #     return res, respath

    # def mergeAndGetMaxres(self, nums1, nums2):
    #     return [max(nums1, nums2).pop(0) for _ in nums1+nums2]

      # res, respath = 0, []
        # if not nums1:
        #     for i in nums2:
        #         res = res*10 + i
        #     return res, nums2
        # elif not nums2:
        #     for i in nums1:
        #         res = res*10 + i
        #     return res, nums1
        # i = j = 0
        # l1, l2 = len(nums1), len(nums2)
        # while i < l1 and j < l2:
        #     if nums1[i] > nums2[j]:
        #         res = res*10 + nums1[i]
        #         respath.append(nums1[i])
        #         i += 1
        #     elif nums1[i] < nums2[j]:
        #         res = res*10 + nums2[j]
        #         respath.append(nums2[j])
        #         j += 1
        #     else:
        #         k1, k2 = i, j
        #         s1, s2 = 0, 0
        #         while k1 < l1 and k2 < l2 and nums1[k1] == nums2[k2]:
        #             s1 = s1*10 + nums1[k1]
        #             s2 = s2*10 + nums2[k2]
        #             k1 += 1
        #             k2 += 1
        #         if k1 < l1 and k2 < l2 and nums1[k1] > nums2[k2]:
        #             res = res*10**(k1-i) + s1
        #             respath += nums1[i:k1]
        #             i = k1
        #         elif k1 < l1 and k2 < l2 and nums1[k1] < nums2[k2]:
        #             res = res*10**(k2-j) + s2
        #             respath += nums2[j:k2]
        #             j = k2
        #         elif k1 >= l1:
        #             res = res*10**(k2-j) + s2
        #             respath += nums2[j:k2]
        #             j = k2
        #         elif k2 >= l2:
        #             res = res*10**(k1-i) + s1
        #             respath += nums1[i:k1]
        #             i = k1

        # if i >= l1:
        #     for n in nums2[j:]:
        #         res = res*10 + n
        #         respath += [n]
        # else:
        #     for n in nums1[i:]:
        #         res = res*10 + n
        #         respath += [n]
        # return res, respath


# @lc code=end

