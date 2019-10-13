#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack, i = [], 0
        while i < len(preorder):
            while len(stack) >= 3 and stack[-1]+stack[-2] == '##':
                if stack[-3] == '#':
                    return False
                stack = stack[:-3]
                stack.append('#')
            stack.append(preorder[i])
            i += 1
        while len(stack) >= 3 and stack[-1]+stack[-2] == '##':
            if stack[-3] == '#':
                return False
            stack = stack[:-3]
            stack.append('#')
        return True if len(stack) == 1 and stack[0] == '#' else False
Accepted
150/150 cases passed (44 ms)
Your runtime beats 49.03 % of python3 submissions
Your memory usage beats 25 % of python3 submissions (13.8 MB)

# if __name__ == "__main__":
#     res = Solution().isValidSerialization("1,#,#,#,#")
# @lc code=end

