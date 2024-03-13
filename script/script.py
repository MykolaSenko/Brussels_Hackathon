


def ask_chat(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return 'Tell me more'