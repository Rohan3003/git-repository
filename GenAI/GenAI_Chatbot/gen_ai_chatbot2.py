# pip install langsmith
# from langsmith import Client

# client = Client()

# import librairies
#import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

open_ai_key = "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"
#os.environ["OPENAI_API_KEY"] = open_ai_key

llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=open_ai_key)

memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory)

print("Chatbot : Hello! How can I assit you today?")

while True:
    user_input = input("You : ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = conversation.run(user_input)
    print(f"Chatbot : {response}")


