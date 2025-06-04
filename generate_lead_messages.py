import json
from src.generate_messages import generate_message

with open("scored_leads.json", "r") as f:
    leads = json.load(f)

enriched_leads = []

for lead in leads:
    score = lead.get("score", 0)
    categories = lead.get("matched_categories", [])
    if not isinstance(categories, list):
        categories = []

    text = lead.get("text", "")

    message = generate_message(text, score, categories)

    # Only include leads with messages (score must be high enough)
    if message:
        enriched_leads.append({
            **lead,              # Keep original lead fields
            "message": message   
        })

# Save enriched leads to new JSON
with open("scored_with_messages.json", "w") as f:
    json.dump(enriched_leads, f, indent=2)
