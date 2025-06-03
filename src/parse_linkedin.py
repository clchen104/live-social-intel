import json
from score_leads import score_tweet
from generate_messages import generate_message

def parse_linkedin_posts(input_file="linkedin_posts.json", output_file="linkedin_scored_with_messages.json"):
    with open(input_file, "r") as f:
        posts = json.load(f)

    scored_leads = []

    for post in posts:
        score, categories = score_tweet(post["text"])
        message = generate_message(post["text"], score, categories)

        if message:
            scored_leads.append({
                "source": "LinkedIn",
                "author": post["author"],
                "text": post["text"],
                "timestamp": post["timestamp"],
                "score": score,
                "matched_categories": categories,
                "message": message
            })

    with open(output_file, "w") as f:
        json.dump(scored_leads, f, indent=2)

if __name__ == "__main__":
    parse_linkedin_posts()
