#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
class Solution:
    def candy(self, ratings) -> int:
        res, des, pre = 1, 0, 1
        for i in range(1, len(ratings)):
            if ratings[i-1] <= ratings[i]:
                if des > 0:
                    res += ((1 + des) * des) // 2  
                    if pre <= des:
                        res += des-pre+1   
                    pre = 1
                    des = 0
                if ratings[i-1] == ratings[i]:
                    pre = 1
                else:
                    pre += 1
                res += pre
            else:
                des += 1
        if des > 0:
            res += ((1 + des) * des) // 2  
            if pre <= des:
                res += des-pre+1  
        return res
✔ Accepted
  ✔ 48/48 cases passed (176 ms)
  ✔ Your runtime beats 92.01 % of python3 submissions
  ✔ Your memory usage beats 40 % of python3 submissions (16.2 MB)

# if __name__ == "__main__":
#     res = Solution().candy([1,3,2,2,1])
