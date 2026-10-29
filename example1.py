from ollama import chat

## Each message has both a role, which can instruct the model as to how to respond, and a content,
## which is the prompt. Here we just send a single message via 'chat' and then get a response.

messages = [
  {
    'role': 'user',
    'content': 'What is the capital of California?',
  },
]

response = chat('orca-mini', messages=messages)
print(response['message']['content'])
print(f"What else in in this response?: {response}")