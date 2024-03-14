import json
from haystack.dataclasses import ChatMessage, ChatRole
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.generators.utils import print_streaming_chunk

def ask_chat(prompt, messages):
    
    chat_generator = OpenAIChatGenerator(model="gpt-3.5-turbo")
    if not messages:
        messages = [
        ChatMessage.from_system(
            """
            You are a social worker specialized in domestic violence.
            You have to always answer in 1 sentence, with a friendly and supportive tone.
            The user talking to you is in Belgium.

            You should make sure you get all this information, one question at a time and in that order:
            - Is the user safe right now?
            - Are there other victims?
            - What are the details of what happened?
            - How long has it been happening?
            - Is the user injured?
            - Does the user have evidence?

            If all the questions have been answered, redirect the user to the house of justice and explain how to contact them.
            """
        )]
    messages.append(ChatMessage.from_user(prompt))
    response = chat_generator.run(messages=messages)
    messages.append(response["replies"][0])
    
    return response["replies"][0].content, messages