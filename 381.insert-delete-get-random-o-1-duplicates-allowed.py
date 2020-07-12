#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
import random, collections
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d, self.l = collections.defaultdict(set), [] 

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self.d:
            self.d[val].add(len(self.l))
            self.l.append(val)
            return False
        else:
            self.d[val].add(len(self.l))
            self.l.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.d:
            return False
        index, lastval = self.d[val].pop(), self.l[-1]
        if len(self.d[val]) == 0:
            self.d.pop(val)
        self.l[index] = lastval
        if lastval in self.d:
            self.d[lastval].add(index)
            self.d[lastval].discard(len(self.l)-1)                  
        self.l.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.l)

Accepted
30/30 cases passed (108 ms)
Your runtime beats 69.2 % of python3 submissions
Your memory usage beats 69.18 % of python3 submissions (19 MB)
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# obj.insert(0)
# obj.remove(0)
# obj.insert(-1)
# obj.remove(0)

# param_2 = obj.remove(1)
# print(obj.getRandom())

# @lc code=end

