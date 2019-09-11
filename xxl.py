
class Solution:
    def __init__(self, x):
        self.res = x
    def solver(self, nums, path):
        self.findmax(nums, path)
        return self.res
    def findmax(self, nums, path):
        a = itertools.groupby(nums)
        nums = []
        for i, j in a:
            nums += [list(j)]
        if not nums:
            self.res = max(self.res, path)
            return
        for i in range(len(nums)):
            self.findmax(self.flatten(nums[:i]+nums[i+1:]), path + len(nums[i])**2)

    def flatten(self, nums):
        res = []
        for i in nums:
            res += i
        return res


if __name__ == "__main__":
    import itertools
    nums = [1,4,2,2,3,3,2,4,1]
    # for i, j in a:
    #     nums += [list(j)]
    # print(nums)
    res = Solution(0).solver(nums, 0)
    print(res)
    

    
    
