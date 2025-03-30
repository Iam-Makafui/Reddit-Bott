import requests
from config import TOGETHER_AI_KEY, TOGETHER_AI_MODEL

def analyze_text(text):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {"Authorization": f"Bearer {TOGETHER_AI_KEY}", "Content-Type": "application/json"}
    data = {
        "model": TOGETHER_AI_MODEL,
        "messages": [{"role": "user", "content": text}]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        json_response = response.json()
        if "choices" in json_response and json_response["choices"]:
            return json_response["choices"][0]["message"]["content"]
    return f"Error: {response.status_code} - {response.text}"
