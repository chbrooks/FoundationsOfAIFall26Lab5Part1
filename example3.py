from ollama import chat

from ollama import chat
messages = [
    {'role': 'system',
     'content': "you are a helful tutor for a college student. Give answers in a form helpful for studying for a final."},
]

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
  print(response.message.content + '\n')