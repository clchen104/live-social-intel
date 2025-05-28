import re

def score_tweet(text):
    score = 0
    text_lower = text.lower()

    if re.search(r"\burgent\b|\bneed (help|now)\b", text_lower):
        score += 4
    if re.search(r"\bhiring\b|\bscaling\b|\blooking for help\b", text_lower):
        score += 3
    if re.search(r"\bai automation\b|\bexpert bottleneck\b", text_lower):
        score += 2

    if score >= 5:
        score += 1

    return score
    
