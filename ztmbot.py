import tweepy
import time
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('tweet liked')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
    # follower.follow()

# print(user.screen_name)
# print(user.followers_count)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
