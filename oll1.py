import requests
import json

generate_endpoint = "http://localhost:11434/api/generate"

data = {
    "model" : "gemma2:2b",
    "prompt" : "In one sentence, who is novak djokovik ?"
}

response = requests.post(generate_endpoint, json=data)

if response.status_code == 200:
    print("Answer:  ", end=" ", flush=True)
    for line in response.iter_lines():
        decode_line = line.decode("utf-8")
        if decode_line:
            try:
                response_data = json.loads(decode_line)
                print(response_data['response'], end="", flush=True)
            except json.JSONDecodeError:
                print("Error decoding JSON response")
else:
    print(f"Error: Request failed with status code {response.status_code}")