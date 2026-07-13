class Twitter:

    def __init__(self):
        # user_id: following
        self.users = defaultdict(set)
        # user_id: tweet_id
        self.posts = defaultdict(list)
        self.time_stamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time_stamp, tweetId))
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = list()
        # get all the userIds that they follow
        following = self.users[userId] # set of all of them unique
        posts = defaultdict(list)
        # now we want the 10 most recent posts from these users
        following.add(userId)
        maxHeap = list()
        # need the most recent post from each user
        for f_id in following:
            if f_id in self.posts:
                index = len(self.posts[f_id]) - 1
                time_stamp, tweetId = self.posts[f_id][index]
                maxHeap.append((-time_stamp, tweetId, f_id, index))

        heapq.heapify(maxHeap)

        # pull a post off the maxHeap
        while len(news_feed) < 10 and maxHeap:
            _, tweetId, poster, index = heapq.heappop(maxHeap)

            # place it into the news feed
            news_feed.append(tweetId)
            # then we need the next most recent post from that user
            index -= 1
            if index >= 0:
                time_stamp, tweetId = self.posts[poster][index]
                heapq.heappush(maxHeap, (-time_stamp, tweetId, poster, index))
        
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

'''
NOTES

post tweet have to have a timestamp has a unique id so that could auto increment

follow/unfollow each person needs a map of who the are following

view 10 most recent tweets (largest time stamp) so maxHeap of some kind

'''