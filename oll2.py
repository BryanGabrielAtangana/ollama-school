from ollama import chat

content = "Who is the king of clay in the world of Tennis ?"

stream = chat(
    model='llama3.2:1b',
    messages=[{'role': 'user', 'content': content }],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)