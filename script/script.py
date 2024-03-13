import streamlit as st

from haystack import Pipeline
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.converters import HTMLToDocument
from haystack.components.builders import PromptBuilder
from haystack.components.generators import OpenAIGenerator

def ask_chat(prompt):
    fetcher = LinkContentFetcher()
    converter = HTMLToDocument()
    prompt_template = """
    Please help me know what to do.
    I'm in Belgium


    My question is: {{query}}
    Please answer in the language of the question.
    """

    # Only use this information:

    # {% for document in documents %}
    # {{document.content}}
    # {% endfor %}

    prompt_builder = PromptBuilder(template=prompt_template)
    llm = OpenAIGenerator()

    pipeline = Pipeline()
    pipeline.add_component("fetcher", fetcher)
    pipeline.add_component("converter", converter)
    pipeline.add_component("prompt", prompt_builder)
    pipeline.add_component("llm", llm)

    pipeline.connect("fetcher.streams", "converter.sources")
    # pipeline.connect("converter.documents", "prompt.documents")
    pipeline.connect("prompt.prompt", "llm.prompt")

    result = pipeline.run({"fetcher": {"urls": ["https://resourcehub.bakermckenzie.com/en/resources/fighting-domestic-violence/europe/belgium/topics/4-protection-for-domestic-violence-victims-and-relief-granted"]},
                "prompt": {"query": prompt}})
    
    return result["llm"]["replies"][0]