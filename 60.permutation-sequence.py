#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i+1) for i in range(n)]
        fac, t = [], 1
        for i in range(1,n):
            t *= i
            fac.append(t)
        res = ''
        for i in range(n-2, -1, -1):
            tmp, r = k // fac[i], k % fac[i]
            k = r
            if r:
                tmp += 1
            res += str(nums.pop(tmp-1))
        res += str(nums[0])
        return res
✔ Accepted
  ✔ 200/200 cases passed (32 ms)
  ✔ Your runtime beats 95.71 % of python3 submissions
  ✔ Your memory usage beats 8.33 % of python3 submissions (13.8 MB)

# if __name__ == "__main__":
#     res = Solution().getPermutation(4, 11)
    
