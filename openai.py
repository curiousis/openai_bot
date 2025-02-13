import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()

key = os.getenv("API_KEY")

max_completion_tokens = 50
temperature = 1

old_data = []


def main():
    while True:
        user_input = input("Input: ")
        if user_input == "stop":
            break
        else:
            response = chatgpt_query(user_input)
            print(response["choices"][0]["message"]["content"])


def chatgpt_query(prompt):
    headers = {"Authorization": "Bearer " + key, "Content-Type": "application/json"}
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "max_completion_tokens": max_completion_tokens,
        "temperature": temperature,
        "model": "gpt-4o",
    }
    old_data.append({"role": "user", "content": prompt})
    data["messages"] = old_data
    r = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        data=json.dumps(data),
    )

    r_json = r.json()
    return r_json


if __name__ == "__main__":
    main()
