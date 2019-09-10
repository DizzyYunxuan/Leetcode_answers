#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
import bisect
class TimeMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key][timestamp] = value
            self.dict[key]['time'].append(timestamp)
        else:
            self.dict[key] = {timestamp:value}
            self.dict[key]['time'] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_left(self.dict[key]['time'], timestamp)
        if idx < len(self.dict[key]['time']) and self.dict[key]['time'][idx] == timestamp:
            return self.dict[key][timestamp]
        elif idx - 1 >= 0:
            return self.dict[key][self.dict[key]['time'][idx-1]]
        else:
            return ''
✔ Accepted
  ✔ 45/45 cases passed (736 ms)
  ✔ Your runtime beats 68.52 % of python3 submissions
  ✔ Your memory usage beats 20 % of python3 submissions (65.3 MB)
# if __name__ == "__main__":
#     tim = TimeMap()
#     tim.set("love","high",10)
#     tim.set("love","low",20)
#     t = tim.get("love",5)
#     t = tim.get("love",10)
#     # tim.set("foo","bar2",4)
#     t = tim.get("love",15)
#     t = tim.get("love",20)
#     t = tim.get("love",25)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

