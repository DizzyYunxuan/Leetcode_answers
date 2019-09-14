#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
class Solution:
    def candy(self, ratings) -> int:
        res = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] += 1
            elif ratings[i] == ratings[i-1]:
                res[i] = 1
            else:
                res[i] -= 1
        s = 0
        if 0 in res:
            for i in res:
                s += i+1
        return s


# if __name__ == "__main__":
#     res = Solution().candy([1,3,2,2,1])
