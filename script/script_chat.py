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

            If all the questions have been answered, redirect the user to the house of justice and explain how to contact them with the following information:
            Phone number: 0800 00 00 00
            """
        )]
    messages.append(ChatMessage.from_user(prompt))
    response = chat_generator.run(messages=messages)
    messages.append(response["replies"][0])
    
    return response["replies"][0].content, messages

    
def ask_status(chat_messages):
    chat_generator = OpenAIChatGenerator(model="gpt-3.5-turbo")

    chat_messages_content = ' '.join(chat_message.content for chat_message in chat_messages)
    # print("chat messages : " + chat_messages_content)
    
    status_prompt = """
        Below is a form with questions about the chat you just had. 
        Please fill it with information provided by the user and what you can infer from it. 
        Answer each element with only 'yes', 'no' or 'not sure yet' followed by your reasonning.

        Here is an example of how to answer each element of that form.
        # First example chat #
        > Hello, how are you
        I'm fine, thank you, what about you?

        # First example of filled form #
        A. Is the user married?: not sure yet
        B. Is the user a child?: not sure yet
        C. Is the user injured?: not sure yet

        # Second example chat #
        > Hello, how are you
        I'm fine, thank you, what about you?
        > Well, my wife is angry at me.
        I'm sorry to hear that.

        # Second example of filled form #
        A. Is the user married?: yes, user mentioned their wife
        B. Is the user a child?: no, a child would not be married
        C. Is the user injured?: not sure yet

        # This is the chat history you should use as input #
    """ + chat_messages_content + """
        # End of the chat history #

        # This is the form you should fill based on the chat history listed above #
        A. Is the user married?: 
        B. Is the user a child?: 
        C. Is the user injured?: 
        # End of the form you should fill #
        """

    messages = [ChatMessage.from_system(status_prompt)]
    response = chat_generator.run(messages=messages)
    return response["replies"][0].content
