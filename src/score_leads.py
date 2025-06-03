import re

def score_tweet(text):
    score = 0
    matched_categories = 0
    text_lower = text.lower()

    # Urgency signals
    if re.search(r"\burgent\b|\bneed (help|now)\b", text_lower):
        score += 2
        matched_categories += 1

    #Hiring/growth signals
    if re.search(r"\bhiring\b|\bscaling\b|\blooking for help\b", text_lower):
        score += 2
        matched_categories += 1

    # AI-relevance signals
    if re.search(r"\bai automation\b|\bexpert bottleneck\b", text_lower):
        score += 2
        matched_categories += 1
    
    # Company size signals
    if re.search(r"\binc\b|\bcorp\b|\bllc\b|\bteam of \d{2,}\b|\bfortune\b", text_lower):
        score += 1
        matched_categories += 1
    
    # Budget/investment signals
    if re.search(r"\bfunded\b|\braising\b|\binvestment\b|\bseries [abc]\b|\blaunching ai\b", text_lower):
        score += 2
        matched_categories += 1

    # Leadership roles
    if re.search(r"\bceo\b|\bcto\b|\bvp\b|\bhead of\b|\bdirector\b", text_lower):
        score += 1
        matched_categories += 1


    if matched_categories >= 3:
        score += 1
    
    score = min(score, 10)

    return score, matched_categories
    
