#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     stack = [root]
    #     res = []
    #     while stack:
    #         cur = stack.pop(0)
    #         if cur:
    #             res.append(str(cur.val))
    #             stack.append(cur.left)
    #             stack.append(cur.right)
    #         else:
    #             res.append('null')
    #     res = '[' + ','.join(res) +']'
    #     return res


    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     data = data[1:-1].split(',')
    #     data = list(map(lambda x: None if x == 'null' else TreeNode(int(x)), data))
    #     root = data.pop(0)
    #     stack = [root]
    #     while data:
    #         cur = stack.pop(0)
    #         cur.left = data.pop(0)
    #         cur.right = data.pop(0)
    #         if cur.left:
    #             stack.append(cur.left)
    #         if cur.right:
    #             stack.append(cur.right)
    #     return root
        # data = map
# ✔ Accepted
#     ✔48/48 cases passed (200 ms)
#     ✔Your runtime beats 9.29 % of python3 submissions
#     ✔Your memory usage beats 24.14 % of python3 submissions (18.9 MB)

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
    
        return rserialize(root, '')


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root 
✔Accepted
    ✔48/48 cases passed (192 ms)
    ✔Your runtime beats 12 % of python3 submissions
    ✔Your memory usage beats 6.9 % of python3 submissions (24.7 MB)
# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.right.left = TreeNode(4)
#     root.right.right = TreeNode(5)
#     codec = Codec()
#     codec.deserialize(codec.serialize(root))
#     print(res)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

