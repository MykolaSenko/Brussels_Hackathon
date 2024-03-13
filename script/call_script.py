import os
from script_chat import ask_chat

# prompt = "Mijn vrouw slaat mij, wat kan ik doen ?"
prompt = "Ma femme me bat, qu'est-ce que je peux faire ?"
# question = "My wife is beating me, what could I do?"

print(prompt)

message_history = []
response, message_history = ask_chat(prompt, message_history)

print(response)

prompt2 = "Est-ce que tu peux expliquer plus en détail ta première proposition stp ?"
response, message_history = ask_chat(prompt2, message_history)

print(response)