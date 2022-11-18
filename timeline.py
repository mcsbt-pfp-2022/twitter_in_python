class Timeline:

    def __init__(self):
        self.tweets = []

    def show_tweets_for(self, user):
        for tweet in self.tweets:
            if tweet.user in user.following:
                print("@"+tweet.user.name + ": " + tweet.message)


    