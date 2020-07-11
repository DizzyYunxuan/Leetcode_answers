#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomset = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.randomset:
            self.randomset[val] = True
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        ret = self.randomset.get(val, False)
        if ret:
            self.randomset.pop(val)
        return ret

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        from random import choice
        if len(self.randomset):
            return choice(list(self.randomset.keys()))
        else:
            return False
 Accepted
18/18 cases passed (396 ms)
Your runtime beats 17.46 % of python3 submissions
Your memory usage beats 87.5 % of python3 submissions (16.7 MB)       
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

