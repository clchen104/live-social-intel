import subprocess

def run(script):
    print(f"Running {script}...")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Finished {script}\n")
    else:
        print(f"Error running {script}:\n{result.stderr}")

def main():
    print("Refreshing tweets and LinkedIn leads...\n")

    # 1. Fetch tweets and score them → scored_leads.json
    run("src/fetch_tweets.py")

    # 2. Generate tweet outreach messages → scored_with_messages.json
    run("generate_lead_messages.py")

    # 3. Score LinkedIn posts + generate messages → linkedin_scored_with_messages.json
    run("src/parse_linkedin.py")

    print("All data refreshed.\n")

if __name__ == "__main__":
    main()
