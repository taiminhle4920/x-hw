import tweepy

# Set your Twitter API credentials
consumer_key = 'tntGkAEbi3jJd0tcRjFNprpBQ'
consumer_secret = 'sfUiSJDBdE5gizUERDaucZeSvqfsU7P11wgH2WiyvlpI4yQQNq'
access_token = '1459835633375932418-7ZUo2JBxWlSfW1JRc1oJ63gBlVwe8R'
access_token_secret = 'z3FG9yjsKgkD5QGfFQmRPImxBy9X1IzWkxhy3gBL5iLpt'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Tweepy API object
api = tweepy.API(auth)

# Create a tweet
def create_tweet(text):
    try:
        tweet = api.update_status(text)
        return tweet.id_str
    except tweepy.errors.TweepyException as e:
        print("Error creating tweet:", e)
        return None

# Retrieve a tweet by its ID
def retrieve_tweet(tweet_id):
    try:
        tweet = api.get_status(tweet_id)
        return tweet.text
    except tweepy.errors.TweepyException as e:
        print("Error retrieving tweet:", e)
        return None

# Delete a tweet by its ID
def delete_tweet(tweet_id):
    try:
        api.destroy_status(tweet_id)
        print("Tweet deleted successfully.")
    except tweepy.errors.TweepyException as e:
        print("Error deleting tweet:", e)

# Example usage
if __name__ == "__main__":
    # Create a tweet
    tweet_id = create_tweet("Hello, Twitter Sandbox!")

    # Retrieve the created tweet
    retrieved_tweet = retrieve_tweet(tweet_id)
    if retrieved_tweet:
        print("Retrieved tweet:", retrieved_tweet)

    # Delete the created tweet
    delete_tweet(tweet_id)
