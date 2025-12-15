import requests
import os
import markdown



def call_api(user_message):
    API_KEY = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    playload = {
        "model": "llama-3.1-8b-instant", 
        "messages": [
            {
                "role": "system",
                "content": "You are a senior software architect."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    }
    try:
        response = requests.post(url=url, headers=headers, json=playload)
        response.raise_for_status()

        response_json = response.json()
        ai_content = response_json['choices'][0]['message']['content']
        htmlready_content = markdown.markdown(ai_content)
        
        return htmlready_content
    except requests.exceptions.RequestException as e :
        print(f"API Request failed: {e}")
        ai_content = f"API Request failed: {e}"
        return ai_content





