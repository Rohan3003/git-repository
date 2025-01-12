openai_key = "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"
from langchain.llms import OpenAI

llm = OpenAI(temperature=0, openai_api_key=openai_key)
name = llm("I want to open a restaurant in New York City. Suggest a fancy name for this restaurant.")
print(name)