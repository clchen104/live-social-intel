import os
import tweepy
from dotenv import load_dotenv
from score_leads import score_tweet
import json

load_dotenv()
#print("BEARER_TOKEN:", repr(os.getenv("TWITTER_BEARER_TOKEN")))
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def search_tweets(query, max_results=10):
    tweets = client.search_recent_tweets(query=query, 
                                        max_results=max_results, 
                                        tweet_fields=["author_id", "created_at"])
    return tweets.data if tweets.data else []

if __name__ == "__main__":
    query = '"AI automation" OR "scaling teams" OR "expert bottlenecks" -is:retweet lang:en'
    results = search_tweets(query, max_results=10)

    for tweet in results:
        score = score_tweet(tweet.text)
        print(f"[{score}/10] {tweet.created_at} | @{tweet.author_id}:\n{tweet.text[:200]}...\n")

scored_data = [
    {
        "score": score_tweet(tweet.text),
        "text": tweet.text,
        "author_id": tweet.author_id,
        "created_at": str(tweet.created_at)
    }
    for tweet in results
]

with open("scored_leads.json", "w") as f:
    json.dump(scored_data, f, indent=2)