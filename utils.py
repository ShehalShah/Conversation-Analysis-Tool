import json
import yaml

def load_conversation(uploaded_file):
    """
    Loads conversation data from an uploaded file (YAML or JSON).
    Detects the file type based on the filename extension.
    """
    file_name = uploaded_file.name
    if file_name.endswith('.json'):
        return json.load(uploaded_file)
    elif file_name.endswith('.yaml') or file_name.endswith('.yml'):
        return yaml.safe_load(uploaded_file)
    return None
