from tweet import Tweet

class User:

    def __init__(self, username, name, bio, timeline):
        self.username = username
        self.name = name
        self.bio = bio
        self.following = set()
        self.timeline = timeline

    def follow(self, user):
        self.following.add(user)

    def tweet(self, message):
        t = Tweet(message, self, 0)
        self.timeline.tweets.append(t)


#%%