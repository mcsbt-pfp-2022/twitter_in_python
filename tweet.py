class Tweet:

    def __init__(self, message, user, timestamp):
        if len(message) > 280:
            raise Exception("character limit exceeded")

        self.message = message
        self.user = user
        self.timestamp = timestamp
        self.likes = 0