import streamlit as st
import json
import traceback
import os
import subprocess

st.set_page_config(page_title="Live Social Leads", layout="wide")

st.title("Live Social Intelligence Leads")

st.markdown("### Refresh Live Leads")
if st.button("Refetch and Rescore"):
    with st.spinner("Fetching new tweets and rescoring..."):
        try:
            subprocess.run(["python", "refresh_all.py"], check=True)
            st.success("Done! Tweets and messages refreshed.")
        except subprocess.CalledProcessError as e:
            st.error("Error while refreshing:")
            st.code(str(e))

def load_json(file):
    try:
        with open(file) as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Failed to load {file}")
        st.code(traceback.format_exc())
        return []

try:
    twitter = load_json("scored_with_messages.json")
    linkedin = load_json("linkedin_scored_with_messages.json")
    combined = twitter + linkedin
    combined = sorted(combined, key=lambda x: x.get("score", 0), reverse=True)
    
    st.markdown("### Top Leads from Twitter and LinkedIn")
    for lead in combined:
        st.subheader(f"{lead.get('author', lead.get('author_id', 'Unknown'))} — {lead['score']}/10")
        st.markdown(f"**Text**: {lead['text']}")
        st.markdown("**Message:**")
        st.markdown(lead["message"])
        st.markdown("---")

except Exception as e:
    st.error("An unexpected error occurred.")
    st.code(traceback.format_exc())
