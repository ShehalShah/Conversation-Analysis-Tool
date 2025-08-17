import re
import requests

def load_profanity_list_from_url(url="https://www.cs.cmu.edu/~biglou/resources/bad-words.txt"):
    """Loads a list of profane words from a URL, filtering out empty lines."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        profane_words = [line for line in response.text.splitlines() if line.strip()]
        return profane_words
    except requests.exceptions.RequestException as e:
        print(f"Error fetching profanity list from URL: {e}")
        return []

def profanity_detection_regex(conversation_data):
    """Identifies profane language and returns the specific words found."""
    profane_words = load_profanity_list_from_url()
    if not profane_words:
        return {"agent_profanity_words": [], "borrower_profanity_words": []}
    
    agent_words_found = set()
    borrower_words_found = set()
    profanity_pattern = r'\b(' + '|'.join(re.escape(word) for word in profane_words) + r')\b'
    
    for utterance in conversation_data:
        text = utterance.get('text', '').lower()
        speaker = utterance.get('speaker', '').lower()
        found_words = re.findall(profanity_pattern, text)
        if found_words:
            if 'agent' in speaker:
                agent_words_found.update(found_words)
            elif 'customer' in speaker or 'borrower' in speaker:
                borrower_words_found.update(found_words)
    return {"agent_profanity_words": list(agent_words_found), "borrower_profanity_words": list(borrower_words_found)}

def compliance_violation_regex(conversation_data):
    """Identifies if agents share sensitive info before identity verification."""
    sensitive_info_pattern = r'\b(balance|due|outstanding|amount is)\b|\$\d+|\d+\s*dollars'
    verification_pattern = r'\b(date of birth|dob|address|social security number|ssn)\b'
    identity_verified = False
    violation_found = False
    for utterance in conversation_data:
        text = utterance.get('text', '').lower()
        speaker = utterance.get('speaker', '').lower()
        if 'agent' in speaker:
            if re.search(verification_pattern, text):
                identity_verified = True
            if re.search(sensitive_info_pattern, text) and not identity_verified:
                violation_found = True
                break
    return {"compliance_violation_found": violation_found}
