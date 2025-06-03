def generate_message(text, score, categories):
    snippet = text.strip().replace("\n", " ")[:100]

    # Use categories to pick message strategy
    if "urgency" in categories and "ai" in categories:
        urgency = "You're clearly facing urgent AI integration needs."
    elif "hiring" in categories and "ai" in categories:
        urgency = "Looks like you're building AI capacity fast."
    elif "urgency" in categories:
        urgency = "Sounds like your team needs help fast."
    elif "budget" in categories and "ai" in categories:
        urgency = "You're investing in AI—let’s make that go further."
    elif score >= 6:
        urgency = "We help teams handle growth and AI expertise gaps."
    else:
        return None

    message = (
    f"Hi there! I saw your recent tweet:\n"
    f' "{snippet}..."\n\n'
    f"{urgency} We help teams integrate AI-human collaboration systems to scale operations and reduce expert bottlenecks.\n\n"
    f"Happy to share a quick demo or talk if you're open!"
)

    return message
