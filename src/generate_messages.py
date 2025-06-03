def generate_message(tweet_text, score):
    snippet = tweet_text.strip().replace("\n", " ")[:100]

    if score >= 9:
        urgency = "It sounds like your team is under serious pressure to scale or automate quickly."
    elif score >= 5:
        urgency = "It seems like you're actively exploring ways to boost team efficiency or handle expertise gaps."
    elif score >= 2:
        urgency = "We noticed you're looking into AI or automation."
    else:
        return None  # Score too low → skip this lead

    message = (
        f"Hi there! I saw your recent tweet:\n"
        f'"{snippet}..."\n\n'
        f"{urgency} We help teams integrate AI-human collaboration systems to scale operations and reduce expert bottlenecks. "
        f" Happy to share a quick demo or talk if you're open!"
    )

    return message
