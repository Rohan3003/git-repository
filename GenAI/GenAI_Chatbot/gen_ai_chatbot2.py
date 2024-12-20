# pip install langsmith
# from langsmith import Client

# client = Client()

# import librairies
#import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

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


