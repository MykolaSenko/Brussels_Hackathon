import os
from script import ask_chat

prompt = "Mijn vrouw slaat mij, wat kan ik doen ?"
# prompt = "Ma femme me bat, qu'est-ce que je peux faire ?"
# question = "My wife is beating me, what could I do?"

print(prompt)

message_history = []
response = ask_chat(prompt, message_history)

print(response.reply_content)

prompt2 = "Are you sure?"
response = ask_chat(prompt2, response.message_history)

