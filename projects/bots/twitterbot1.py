import tweepy

import time

with open('api_key.txt', 'r') as file:
    api_key = file.readline().strip()
    api_secrete = file.readline().strip()
    access_token = file.readline().strip()
    token_secret = file.readline().strip()
    

print(api_key, api_secrete, access_token, token_secret)
auth = tweepy.OAuthHandler(api_key, api_secrete)
auth.set_access_token(access_token, token_secret)

api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.followers_count)
# public_tweets = api.home_timeline()
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

# genrous bot follow back
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    #loop through all the followers
    print(follower.name)
