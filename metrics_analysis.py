import pandas as pd

def calculate_call_metrics(conversation_data):
    """Calculates total duration, silence percentage, and overtalk percentage."""
    if not conversation_data:
        return {"total_duration": 0, "silence_percentage": 0, "overtalk_percentage": 0}
    
    sorted_utterances = sorted(conversation_data, key=lambda x: x['stime'])
    total_duration = max(u['etime'] for u in sorted_utterances) if sorted_utterances else 0
    
    if total_duration == 0:
        return {"total_duration": 0, "silence_percentage": 100, "overtalk_percentage": 0}

    # --- Calculate Silence ---
    total_silence = sorted_utterances[0]['stime']
    last_end_time = 0
    for utterance in sorted_utterances:
        if utterance['stime'] > last_end_time:
            total_silence += (utterance['stime'] - last_end_time)
        last_end_time = max(last_end_time, utterance['etime'])
    silence_percentage = (total_silence / total_duration) * 100

    # --- Calculate Overtalk ---
    df = pd.DataFrame(sorted_utterances)
    total_overtalk = 0
    for i in range(len(df) - 1):
        current_utterance_end = df.loc[i, 'etime']
        next_utterance_start = df.loc[i+1, 'stime']
        if next_utterance_start < current_utterance_end:
            overtalk_duration = current_utterance_end - next_utterance_start
            total_overtalk += overtalk_duration
    overtalk_percentage = (total_overtalk / total_duration) * 100
    
    return {
        "total_duration": round(total_duration, 2),
        "silence_percentage": round(silence_percentage, 2),
        "overtalk_percentage": round(overtalk_percentage, 2)
    }
