import re

def score_tweet(text):
    score = 0
    matched_categories = []
    text_lower = text.lower()

    if re.search(r"\burgent\b|\bneed (help|now)\b", text_lower):
        score += 2
        matched_categories.append("urgency")

    if re.search(r"\bhiring\b|\bscaling\b|\blooking for help\b", text_lower):
        score += 2
        matched_categories.append("hiring")

    if re.search(r"\bai automation\b|\bexpert bottleneck\b", text_lower):
        score += 2
        matched_categories.append("ai")

    if re.search(r"\binc\b|\bcorp\b|\bllc\b|\bteam of \d{2,}\b|\bfortune\b", text_lower):
        score += 1
        matched_categories.append("company_size")

    if re.search(r"\bfunded\b|\braising\b|\binvestment\b|\bseries [abc]\b|\blaunching ai\b", text_lower):
        score += 2
        matched_categories.append("budget")

    if re.search(r"\bceo\b|\bcto\b|\bvp\b|\bhead of\b|\bdirector\b", text_lower):
        score += 1
        matched_categories.append("exec")

    if len(matched_categories) >= 3:
        score += 1

    return score, matched_categories
