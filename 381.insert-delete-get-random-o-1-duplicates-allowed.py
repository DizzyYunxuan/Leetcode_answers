#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
<<<<<<< HEAD
=======
import random
>>>>>>> 0739e97a0d9fd2b36a9817ce96f16e8992944020
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
<<<<<<< HEAD
=======
        self.d, self.l = {}, []

>>>>>>> 0739e97a0d9fd2b36a9817ce96f16e8992944020
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.d.get(val, 0):
            self.d[val] -= 1 
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        l = []
        for k, v in self.d.items():
            l += [k] * v
        rand = random.randint(0, len(l) - 1)
        return l[rand]

Accepted
28/28 cases passed (3116 ms)
Your runtime beats 5.1 % of python3 submissions
Your memory usage beats 98.72 % of python3 submissions (17.7 MB)

# Your RandomizedCollection object will be instantiated and called as such:
# import random
# obj = RandomizedCollection()

# print(obj.insert(1))
# print(obj.insert(1))
# print(obj.insert(2))
# print(obj.getRandom())
# print(obj.remove(1))
# print(obj.getRandom())

# param_1 = obj.getRandom()
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

