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
            Please help me know what to do.
        I'm in Belgium
        """
        )
        ]
    messages.append(ChatMessage.from_user(prompt))
    response = chat_generator.run(messages=messages)
    messages.append(response["replies"][0])
    
    return response["replies"][0].content, messages