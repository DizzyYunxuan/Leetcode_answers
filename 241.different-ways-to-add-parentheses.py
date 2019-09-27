#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#




import functools
class Solution:
    # @functools.lru_cache(None)
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i, opt in enumerate(input):
            if opt in {"+", "-", "*"}:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                res.extend([self.helper(l, r, opt) for l in left for r in right])
        return res
    def helper(self, m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n

# class Solution:
#     def diffWaysToCompute(self, inputs: str):
#         self.res = []
#         nums_op = []
#         i, start = 0, 0
#         while i < len(inputs):
#             if inputs[i] in '+-*':
#                 nums_op.append(inputs[start:i])
#                 nums_op.append(inputs[i])
#                 start = i+1
#             i += 1
#         nums_op.append(inputs[start:i])
#         self.dfs(nums_op)
#         return self.res
    
#     def dfs(self, nums_ops):
#         if len(nums_ops) == 1:
#             self.res.append(nums_ops[0])
#             return 
        
#         for i in range(len(nums_ops)):
#             if nums_ops[i] == '+':
#                 t = int(nums_ops[i-1]) + int(nums_ops[i+1])
#             elif nums_ops[i] == '-':
#                 t = int(nums_ops[i-1]) - int(nums_ops[i+1])
#             elif nums_ops[i] == '*':
#                 t = int(nums_ops[i-1]) * int(nums_ops[i+1])
#             else:
#                 continue
#             self.dfs(nums_ops[:i-1] + [t] + nums_ops[i+2:])

        # from itertools import permutations
        # opidx = []
        # nums_op = []
        # i, start = 0, 0
        # while i < len(inputs):
        #     if inputs[i] in '+-*':
        #         nums_op.append(inputs[start:i])
        #         nums_op.append(inputs[i])
        #         opidx.append(i)
        #         start = i+1
        #     i += 1
        # nums_op.append(inputs[start:i])
        # all_permutation = permutations(opidx, len(opidx))
        # res = []
        # for per in all_permutation:
        #     t = nums_op.copy()
        #     for opix in per:
        #         op = nums_op[opix]
        #         if op == '*':
        #             t.insert(opix+2, int(t[opix-1]) * int(t[opix+1]))
        #         elif op == '+':
        #             t.insert(opix+2, int(t[opix-1]) + int(t[opix+1]))
        #         else:
        #             t.insert(opix+2, int(t[opix-1]) - int(t[opix+1]))
        #         t[opix-1:opix+2] = []
        #     res.append(t[-1])
        # return res

if __name__ == "__main__":
    res = Solution().diffWaysToCompute("2*3-4*5")
    

