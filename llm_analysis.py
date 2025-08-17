import json
import requests

def format_conversation_for_llm(conversation_data):
    """Formats the conversation data into a simple string transcript."""
    transcript = ""
    for utterance in conversation_data:
        speaker = utterance.get('speaker', 'Unknown')
        text = utterance.get('text', '')
        transcript += f"{speaker}: {text}\n"
    return transcript

def call_openrouter_llm(api_key, model_name, prompt):
    """Generic function to call the OpenRouter API and get a JSON response."""
    api_url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"}
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        message_content = result['choices'][0]['message']['content']
        return json.loads(message_content)
    except requests.exceptions.HTTPError as http_err:
        error_details = response.text
        return {"error": f"HTTP error occurred: {http_err}. Details: {error_details}"}
    except Exception as e:
        return {"error": f"An error occurred with the OpenRouter API: {str(e)}"}

def profanity_detection_llm(conversation_data, api_key):
    """Detects profanity using the specified OpenRouter LLM."""
    transcript = format_conversation_for_llm(conversation_data)
    prompt = (
        "Analyze the following conversation transcript. Identify if the 'Agent' or the 'Customer' "
        "used any profane, offensive, or curse words. "
        "Respond ONLY with a valid JSON object with two keys: 'agent_profanity_found' and 'borrower_profanity_found'. "
        "The value for each should be a boolean (true or false)."
        f"\n\nTranscript:\n{transcript}"
    )
    model_name = "mistralai/mistral-small-3.2-24b-instruct:free"
    return call_openrouter_llm(api_key, model_name, prompt)

def compliance_violation_llm(conversation_data, api_key):
    """Detects compliance violations using the specified OpenRouter LLM."""
    transcript = format_conversation_for_llm(conversation_data)
    prompt = (
        "You are a compliance analysis bot. Your task is to determine if the 'Agent' shared sensitive account details "
        "(like a balance, amount due, etc.) *before* properly verifying the customer's identity by asking for a "
        "date of birth, address, or Social Security Number. A phone number is NOT a valid verification method. "
        "Analyze the following transcript and respond ONLY with a valid JSON object with one key: 'compliance_violation_found', "
        "and a boolean value (true or false)."
        f"\n\nTranscript:\n{transcript}"
    )
    model_name = "mistralai/mistral-small-3.2-24b-instruct:free"
    return call_openrouter_llm(api_key, model_name, prompt)
