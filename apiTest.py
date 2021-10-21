import tweepy 

auth = tweepy.OAuthHandler("5iMa6JgOPXNpORWuXrMKI0UcU", "FNOpLutXbEUHmxV0lOwXpDeNmwfR6flibTPYJGo2eyEHNk5rvV")
auth.set_access_token("1450877804606857223-OyxOia0nz2p8sE9icr4lXpMvwM6NQY", "x5ibgpklb1lq3Kf0B7DaF1VOD6AcKQjK7LoXwpU2Q0V2g")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text.encode('utf-8'))