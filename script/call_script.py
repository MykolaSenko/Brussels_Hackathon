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
prompt = """
        Please fill this form with confirmed information about the user that you are sure about based on the chat so far. Answer each element with only 'yes', 'no' or 'not sure yet'.
        For example
        - Is the moon full?: not sure yet
        - Is the user married?: yes
        - Is the user a child?: no

        Here are my actual questions:
        - Is the user married?: 
        - Is the user a child?: 
        """
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


