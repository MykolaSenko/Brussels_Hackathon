import os
from script_chat import ask_chat

message_history = []

prompt = "Hello, I need help"
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")

prompt = "Yes"
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")

prompt = "No"
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")

prompt = "My wife beats me all the time"
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")

prompt = "Since marriage, 2 years ago. She beats me every day in the morning before leaving to work."
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")

#### SYSTEM ####
prompt = "Is the user married? Answer with yes or no."
print("[System] " + prompt)
response, _ = ask_chat(prompt, message_history)
print(response + "\n")

prompt = "Yes, I even went to the hospital last week!"
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")

prompt = "Well, I have the hospital bills"
print("> " + prompt)
response, message_history = ask_chat(prompt, message_history)
print(response + "\n")


