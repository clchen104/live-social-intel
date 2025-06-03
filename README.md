# Live Social Intelligence System

This project is a real-time social intelligence tool that monitors **Twitter** and **LinkedIn** for urgent business signals — helping identify companies and professionals who may need **AI + human expert collaboration solutions**.

Built to address real-world lead generation challenges with Moccet's platform in mind.

---

## Demo

**Live App**: [https://clchen104-live-social-intel-streamlit-app-w8ryza.streamlit.app/](https://clchen104-live-social-intel-streamlit-app-w8ryza.streamlit.app/)  
**GitHub Repo**: [https://github.com/clchen104/live-social-intel](https://github.com/clchen104/live-social-intel)

---

## Features

- 🔍 **Monitors Twitter and LinkedIn** for keywords like `AI automation`, `scaling teams`, `expert bottlenecks`
- **Regex-based scoring model** to detect:
  - Urgency signals
  - Hiring and scaling intent
  - Budget/investment readiness
  - Leadership and company indicators
- **Generates custom outreach messages** based on lead profile

---

## How It Works

1. **Twitter ingestion**  
   Uses the Twitter API to fetch recent tweets containing target signals

2. **(Optional) LinkedIn ingestion**  
   Parses preloaded mock `linkedin_posts.json` for demo purposes

3. **Scoring**  
   Applies a modular scoring system to assign weights and categories

4. **Message generation**  
   Custom messages are generated based on matched intent

5. **Streamlit dashboard**  
   Displays top leads and personalized messages in a clean UI

---

## Try It Locally

### 1. Clone the repo

```bash
git clone https://github.com/clchen104/live-social-intel.git
cd live-social-intel
