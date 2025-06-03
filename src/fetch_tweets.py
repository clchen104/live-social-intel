import os
import tweepy
from dotenv import load_dotenv
from score_leads import score_tweet
import json

load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def search_tweets(query, max_results=10):
    try:
        response = client.search_recent_tweets(
            query=query, 
            max_results=max_results, 
            tweet_fields=["author_id", "created_at"]
        )
        
        if response.data is None:
            print("Twitter returned no data. Using fallback.")
            raise Exception("Empty response from Twitter API.")

        return response.data

    except tweepy.TooManyRequests:
        print("Twitter API rate limit hit (HTTP 429). Falling back to mock tweets.")

    except Exception as e:
        print("Error fetching tweets:", e)
        print("Falling back to mock tweets.")

    # Fallback: load mock tweets
    try:
        print("Using mock tweets for scoring.")
        with open("mock_tweets.json", "r") as f:
            mock_tweets = json.load(f)
            print(f"Loaded {len(mock_tweets)} mock tweets.")
            return mock_tweets
    except Exception as e:
        print("Failed to load mock tweets:", e)
        return []


if __name__ == "__main__":
    query = '"AI automation" OR "scaling teams" OR "expert bottlenecks" -is:retweet lang:en'
    results = search_tweets(query, max_results=10)

    if not results:
        print("No tweets to score. Skipping save.")
        exit()

    scored_data = []
    for tweet in results:
        # Handle both real tweets and mock tweet dicts
        if isinstance(tweet, dict):
            text = tweet["text"]
            author = tweet.get("author_id", "mock")
            created = tweet.get("created_at", "mock")
        else:
            text = tweet.text
            author = tweet.author_id
            created = str(tweet.created_at)

        score, categories = score_tweet(text)
        scored_data.append({
            "score": score,
            "matched_categories": categories,
            "text": text,
            "author_id": author,
            "created_at": created
        })

    # Save results to JSON
    with open("scored_leads.json", "w") as f:
        json.dump(scored_data, f, indent=2)
        print(f"Saved {len(scored_data)} leads to scored_leads.json")
