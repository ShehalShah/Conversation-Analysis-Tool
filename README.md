# 📞 Conversation Analysis Tool for Debt Collection

A **Streamlit web application** designed to analyze conversation transcripts between debt collection agents and borrowers.  
It evaluates **compliance, professionalism, and call quality metrics** using both:

- **Pattern-Matching (Regex)**  
- **Machine Learning (LLM)** — powered by [Mistral via OpenRouter](https://openrouter.ai/)  

---

## ✨ Features

### 🔹 Profanity Detection
- **Regex Approach**: Matches against a dynamically-loaded profanity wordlist.  
- **LLM Approach**: Uses contextual AI to detect profanity beyond wordlists.

### 🔹 Privacy & Compliance Violation
- Detects if an **agent shares sensitive account info** (e.g., balance) before verifying customer identity.
- **Regex Approach**: Searches for keywords in the required sequence.  
- **LLM Approach**: Analyzes conversation flow for compliance breaches.

### 🔹 Call Quality Metrics
- **Silence Percentage**: % of call duration with no speech.  
- **Overtalk Percentage**: % of call with simultaneous speech.  
- Results are **visualized interactively** in the UI.

### 🔹 Interactive Web Interface
- Upload **JSON/YAML** conversation transcripts.  
- Select **analysis type** (Profanity, Compliance, Metrics).  
- Choose **analysis approach** (Regex or LLM).  
- View results instantly in your browser.

---

## 📂 Project Structure

