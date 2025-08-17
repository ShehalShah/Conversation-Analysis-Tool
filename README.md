# Conversation Analysis Tool for Debt Collection

This project is a **Streamlit web application** designed to analyze conversation transcripts between debt collection agents and borrowers.
It evaluates **compliance, professionalism, and call quality metrics** using both **pattern-matching (Regex)** and **machine learning (LLM)** approaches, as per the assignment requirements.

Deployed Link: https://conversation-analysis-tool-assignment.streamlit.app/
---

## 🚀 Features

### 🔹 Profanity Detection

* Identifies profane language used by either the agent or the borrower.
* **Regex Approach**: Uses a comprehensive, dynamically-loaded wordlist to find specific profane words.
* **LLM Approach**: Leverages a large language model (Mistral via OpenRouter) to understand context and detect profanity.

### 🔹 Privacy & Compliance Violation

* Detects if an agent shared sensitive account information (e.g., balance) before verifying the customer's identity.
* **Regex Approach**: Looks for keywords related to sensitive info and identity verification in a specific order.
* **LLM Approach**: Uses AI to analyze the conversational flow for compliance breaches.

### 🔹 Call Quality Metrics

* **Silence Percentage**: Percentage of call duration where no one was speaking.
* **Overtalk Percentage**: Percentage of call duration where both parties spoke simultaneously.
* Visualizations of these metrics are generated inside the app.

### 🔹 Interactive UI

* Built with **Streamlit** for a user-friendly web interface.
* Features:

  * File uploads (`.json` or `.yaml` transcripts)
  * Selection of analysis methods
  * Sidebar API key entry
  * Results displayed on the main panel

---

## 📂 Project Structure

```
solution_engineer_project/
│
├── app.py                # Main Streamlit application
├── regex_analysis.py     # Functions for the Regex approach
├── llm_analysis.py       # Functions for the LLM approach
├── metrics_analysis.py   # Functions for call quality metrics
├── utils.py              # Utility functions (e.g., file loading)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── Technical_Report.md   # Technical report
```

## ⚙️ Setup and Execution

### ✅ Prerequisites

* Python **3.8+**
* An **OpenRouter API Key** (for LLM features)

---

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### 2. Create and Activate a Virtual Environment

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

Your browser should open at:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🖥️ Using the Application

1. **Enter your API Key**: Paste your OpenRouter API key in the sidebar (required for "Machine Learning (LLM)" analysis).
2. **Upload a File**: Provide a conversation transcript in `.json` or `.yaml` format.
3. **Select Analysis Type**:

   * Profanity Detection
   * Compliance Check
   * Call Quality Metrics
4. **Choose Approach** (if applicable):

   * Pattern Matching (**Regex**)
   * Machine Learning (**LLM**)
5. **View Results**: Results and metrics will be displayed in the main panel.

---

## 📌 Notes

* Regex-based analysis is fast but limited to keyword rules.
* LLM-based analysis is more context-aware but requires an **API key** and internet connectivity.
* Call quality metrics are computed from transcript timing metadata.

---

## 📝 License

This project is for **educational and assignment purposes** only.
All external APIs and libraries used must comply with their respective licenses.
