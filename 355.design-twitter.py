#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeStamp = 0
        self.tweetTimeLine = {}
        self.followList = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.timeStamp -= 1
        self.tweetTimeLine[userId] = self.tweetTimeLine.get(userId, []) + [[self.timeStamp, tweetId]]

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.followList:
            self.followList[userId] = [userId]
        res = []

        for user in self.followList[userId]:
            if self.tweetTimeLine.get(user, [user]):
                res += self.tweetTimeLine.get(user, [])
        res.sort()
        res = res[:10]
        # print(res)
        return [i[1] for i in res]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.followList.get(followerId, [followerId]):
            self.followList[followerId] = self.followList.get(followerId, [followerId]) + [followeeId]
        # print(self.followList)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId and followeeId in self.followList.get(followerId, []):
            self.followList[followerId].remove(followeeId)
        # print(self.followList)
Accepted
23/23 cases passed (84 ms)
Your runtime beats 95.14 % of python3 submissions
Your memory usage beats 42.1 % of python3 submissions (18.4 MB)

# if __name__ == "__main__":
#     obj = Twitter()
#     obj.postTweet(1,5)
#     obj.postTweet(2,3)
#     obj.postTweet(1,101)
#     obj.postTweet(2,13)
#     obj.postTweet(2,10)
#     obj.postTweet(1,2)
#     obj.postTweet(1,94)
#     obj.postTweet(2,505)
#     obj.postTweet(1,333)
#     obj.postTweet(2,22)
#     obj.postTweet(1,11)
#     obj.postTweet(1,205)
#     obj.postTweet(2, 203)
#     obj.postTweet(1,201)
#     obj.postTweet(2,213)
#     obj.postTweet(1,200)
#     obj.postTweet(2,202)
#     obj.postTweet(1,204)
#     obj.postTweet(2,208)
#     obj.postTweet(2,233)
#     obj.postTweet(1,222)
#     obj.postTweet(2,211)
#     param_2 = obj.getNewsFeed(1)
#     obj.follow(1,2)
#     param_2 = obj.getNewsFeed(1)
#     obj.unfollow(1,2) 
#     param_2 = obj.getNewsFeed(1)
#     print(1)
    # # obj.postTweet(2, 6)
    # param_2 = obj.getNewsFeed(2)
#     # param_2 = obj.getNewsFeed(1)
#     obj.unfollow(2,1) 
#     obj.getNewsFeed(2)
    # print(1)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

