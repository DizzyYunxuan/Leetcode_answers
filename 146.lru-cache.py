#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.d = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            v = self.d.pop(key)
            self.d[key] = v
            return v

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.d.popitem(last=False)
        self.d[key] = value
✔ Accepted
  ✔ 18/18 cases passed (212 ms)
  ✔ Your runtime beats 76.43 % of python3 submissions
  ✔ Your memory usage beats 6.06 % of python3 submissions (22.5 MB)



# if __name__ == "__main__":
#     operations = input().split(',')
#     vals = input().split('],[')
#     for i in range(len(vals)):
#         if vals[i][0] == '[':
#             vals[i] = vals[i][1:]
#         elif vals[i][-1] == ']':
#             vals[i] = vals[i][:-1]
#         vals[i] = list(map(int, vals[i].split(',')))

        
#     opval = zip(operations, vals)

#     for op, val in opval:
#         if op == '"LRUCache"':
#             cache = LRUCache(val[0])
#         elif op == '"get"':
#             cache.get(val[0])
#         elif op == '"put"':
#             cache.put(val[0], val[1])
#         else:
#             raise ValueError
    
# "LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"
# [10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

