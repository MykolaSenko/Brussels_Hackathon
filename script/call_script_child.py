import os
from script_chat import ask_chat, ask_status

message_history = []

prompt = "Hello, I need help"
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")

#### SYSTEM ####
response = ask_status(message_history)
print("[System]" + "\n" + response + "\n")

prompt = "Yes"
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")

prompt = "No, it's just me, I got beaten up when I came back from school"
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")

#### SYSTEM ####
response = ask_status(message_history)
print("[System]" + "\n" + response + "\n")

