from openai import OpenAI

openai = OpenAI(
    api_key="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"
)

response = openai.chat.completions.create(model="gpt-4o-mini", messages=[
    {'role': 'system', 'content': 'You are a helpful assistant.'},
])

print(response)