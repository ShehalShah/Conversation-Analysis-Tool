Conversation Analysis Tool for Debt Collection
This project is a Streamlit web application designed to analyze conversation transcripts between debt collection agents and borrowers. It evaluates compliance, professionalism, and call quality metrics using both pattern-matching (Regex) and machine learning (LLM) approaches, as per the assignment requirements.

Features
Profanity Detection: Identifies profane language used by either the agent or the borrower.

Regex Approach: Uses a comprehensive, dynamically-loaded wordlist to find specific profane words.

LLM Approach: Leverages a large language model (Mistral via OpenRouter) to understand context and detect profanity.

Privacy and Compliance Violation: Detects if an agent shared sensitive account information (e.g., balance) before verifying the customer's identity.

Regex Approach: Looks for keywords related to sensitive info and identity verification in a specific order.

LLM Approach: Uses AI to analyze the conversational flow for compliance breaches.

Call Quality Metrics: Calculates and visualizes key call metrics.

Silence Percentage: The percentage of the call duration where no one was speaking.

Overtalk Percentage: The percentage of the call where both parties were speaking simultaneously.

Interactive UI: A user-friendly web interface built with Streamlit that allows for file uploads and selection of analysis methods.

Project Structure
solution_engineer_project/
|
|-- app.py                  # Main Streamlit application
|-- regex_analysis.py       # Functions for the Regex approach
|-- llm_analysis.py         # Functions for the LLM approach
|-- metrics_analysis.py     # Functions for call quality metrics
|-- utils.py                # Utility functions (e.g., file loading)
|-- requirements.txt        # Python dependencies
|-- README.md               # This file
|-- Technical_Report.md     # The technical report

Setup and Execution
Follow these steps to set up and run the project locally.

Prerequisites
Python 3.8 or higher

An OpenRouter API Key (for the LLM features)

1. Clone the Repository
git clone <your-repository-url>
cd <your-repository-name>

2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

3. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

pip install -r requirements.txt

4. Run the Streamlit Application
Launch the application using the following command:

streamlit run app.py

Your web browser should automatically open to the application's URL (usually http://localhost:8501).

5. Using the Application
Enter your API Key: Paste your OpenRouter API key in the sidebar. This is required to use the "Machine Learning (LLM)" approach.

Upload a File: Upload a conversation transcript in either JSON or YAML format.

Select Analysis Type: Choose what you want to analyze (Profanity, Compliance, or Metrics).

Select Approach: If applicable, choose between "Pattern Matching (Regex)" and "Machine Learning (LLM)".

The results will be displayed on the main panel.