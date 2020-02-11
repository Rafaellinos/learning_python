import tweepy

import time

with open('api_key.txt', 'r') as file:
    api_key = file.readline().strip()
    api_secrete = file.readline().strip()
    access_token = file.readline().strip()
    token_secret = file.readline().strip()
    
auth = tweepy.OAuthHandler(api_key, api_secrete)
auth.set_access_token(access_token, token_secret)

api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.followers_count)
# public_tweets = api.home_timeline() # list all twitter in home
# for tweet in public_tweets:
#     print(tweet.text)

def limit_handler(cursor):
    """
        twitter hava a limit of requests per time
        this function will receive cursos and yield
        to the next action, but if gets RateLimitError,
        it sleeps 1s.
    """
    try:    
        while 1:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

# # genrous bot follow back
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     #loop through all the followers
#     print(follower.name)
#     follower.follow() # follows back each follower that u have

search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    # returns the twetts that matches the search
    # try to find all tweets with the search string
    # numbersOfTweets is the number of times that we will search
    try:
        tweet.favorite() # or can retweet()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break