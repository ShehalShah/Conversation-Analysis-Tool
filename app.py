import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Import functions from the new analysis files
from utils import load_conversation
from regex_analysis import profanity_detection_regex, compliance_violation_regex
from llm_analysis import profanity_detection_llm, compliance_violation_llm
from metrics_analysis import calculate_call_metrics

st.set_page_config(layout="wide")
st.title("🗣️ Conversation Analysis Tool for Debt Collection")

st.info("This tool analyzes call transcripts to evaluate compliance, professionalism, and call quality metrics using both Regex and AI.")

# --- Sidebar for User Inputs ---
with st.sidebar:
    st.header("Controls")
    uploaded_file = st.file_uploader(
        "Upload a conversation file (YAML or JSON)",
        type=['yaml', 'yml', 'json']
    )
    
    api_key = st.text_input("Enter your OpenRouter API Key", type="password", help="Required for the Machine Learning (LLM) approach.")

    if uploaded_file:
        analysis_entity = st.selectbox(
            "Select Analysis Type",
            ("Profanity Detection", "Privacy and Compliance Violation", "Call Quality Metrics")
        )

        approach = None
        if analysis_entity in ["Profanity Detection", "Privacy and Compliance Violation"]:
            approach = st.selectbox(
                "Select Approach",
                ("Pattern Matching (Regex)", "Machine Learning (LLM)")
            )

# --- Main Panel for Displaying Results ---
if uploaded_file:
    conversation_data = load_conversation(uploaded_file)
    
    if not conversation_data:
        st.warning("The uploaded file is empty, invalid, or has an unsupported format.")
    else:
        with st.expander("View Full Conversation Transcript"):
            df = pd.DataFrame(conversation_data)
            st.dataframe(df)

        st.markdown("---")
        st.subheader(f"Results for: {analysis_entity}")

        # --- Profanity Detection ---
        if analysis_entity == "Profanity Detection":
            if approach == "Pattern Matching (Regex)":
                st.write("#### Using Pattern Matching (Regex)")
                result = profanity_detection_regex(conversation_data)
                agent_words = result.get("agent_profanity_words", [])
                if agent_words:
                    st.error(f"🚩 Profanity Detected: Agent used the following word(s): **{', '.join(agent_words)}**")
                else:
                    st.success("✅ No profanity detected from the Agent.")
                
                borrower_words = result.get("borrower_profanity_words", [])
                if borrower_words:
                    st.error(f"🚩 Profanity Detected: Borrower used the following word(s): **{', '.join(borrower_words)}**")
                else:
                    st.success("✅ No profanity detected from the Borrower.")

            elif approach == "Machine Learning (LLM)":
                st.write("#### Using Machine Learning (LLM)")
                if not api_key:
                    st.warning("Please enter your OpenRouter API Key to use the LLM approach.")
                else:
                    with st.spinner("The AI is analyzing the transcript..."):
                        result = profanity_detection_llm(conversation_data, api_key)
                        if "error" in result:
                            st.error(result["error"])
                        else:
                            if result.get("agent_profanity_found"):
                                st.error("🚩 Profanity Detected: The AI determined the Agent used profane language.")
                            else:
                                st.success("✅ No profanity detected from the Agent.")
                            
                            if result.get("borrower_profanity_found"):
                                st.error("🚩 Profanity Detected: The AI determined the Borrower used profane language.")
                            else:
                                st.success("✅ No profanity detected from the Borrower.")

        # --- Privacy and Compliance Violation ---
        elif analysis_entity == "Privacy and Compliance Violation":
            if approach == "Pattern Matching (Regex)":
                st.write("#### Using Pattern Matching (Regex)")
                result = compliance_violation_regex(conversation_data)
                if result.get("compliance_violation_found"):
                    st.error("🚩 Violation Detected: Agent shared sensitive info before proper identity verification.")
                else:
                    st.success("✅ No compliance violation detected.")

            elif approach == "Machine Learning (LLM)":
                st.write("#### Using Machine Learning (LLM)")
                if not api_key:
                    st.warning("Please enter your OpenRouter API Key to use the LLM approach.")
                else:
                    with st.spinner("The AI is analyzing the transcript..."):
                        result = compliance_violation_llm(conversation_data, api_key)
                        if "error" in result:
                            st.error(result["error"])
                        else:
                            if result.get("compliance_violation_found"):
                                st.error("🚩 Violation Detected: The AI determined that the Agent shared sensitive info before proper identity verification.")
                            else:
                                st.success("✅ No compliance violation detected.")

        # --- Call Quality Metrics ---
        elif analysis_entity == "Call Quality Metrics":
            metrics = calculate_call_metrics(conversation_data)
            st.write("Analysis of simultaneous speaking (overtalk) and periods of silence.")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Duration (seconds)", f"{metrics['total_duration']}s")
            col2.metric("Silence Percentage", f"{metrics['silence_percentage']}%")
            col3.metric("Overtalk Percentage", f"{metrics['overtalk_percentage']}%")
            
            fig = go.Figure(go.Indicator(mode="gauge+number", value=metrics['silence_percentage'], title={'text': "Silence %"}, domain={'x': [0, 1], 'y': [0, 1]}, gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "lightblue"}}))
            fig.update_layout(height=250)
            st.plotly_chart(fig, use_container_width=True)

            fig2 = go.Figure(go.Indicator(mode="gauge+number", value=metrics['overtalk_percentage'], title={'text': "Overtalk %"}, domain={'x': [0, 1], 'y': [0, 1]}, gauge={'axis': {'range': [None, 100]}, 'bar': {'color': "lightcoral"}}))
            fig2.update_layout(height=250)
            st.plotly_chart(fig2, use_container_width=True)

else:
    st.info("Please upload a conversation file and enter your API key to begin analysis.")
