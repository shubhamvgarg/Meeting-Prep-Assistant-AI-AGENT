import streamlit as st
from graph import build_graph

app_graph = build_graph()

st.title("Meeting Prep Assistant")
title = st.text_input("Meeting Title")
company = st.text_input("Company Name")
participants = st.text_area("Participants (comma-separated)")
excepted_outcome = st.text_area("Brief about meeting what we are aiming from this meeting")
goal = st.selectbox(
    "Meeting Goal",
    ["Sales", "Interview", "Partnership", "General","Training","Discussion"]
)

if st.button("Generate Prep"):
    with st.spinner("Analyzing..."):

        result = app_graph.invoke({
            "title": title,
            "company": company,
            "participants": [p.strip() for p in participants.split(",")],
            "goal": goal,
            "expected_outcome":excepted_outcome
        })

        st.subheader("📄 Meeting Brief")
        st.write(result["brief"])