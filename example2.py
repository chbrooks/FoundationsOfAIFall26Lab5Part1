from ollama import chat
messages = []

while True:
  user_input = input('Chat with history: ')
  response = chat(
    'llama3.1',
    messages=[*messages, {'role': 'user', 'content': user_input}],
  )

  # Add the response to the messages to maintain the history
  messages += [
    {'role': 'user', 'content': user_input},
      {'role': 'assistant', 'content': response.message.content},
  ]
  print(messages)
  print(response.message.content + '\n')