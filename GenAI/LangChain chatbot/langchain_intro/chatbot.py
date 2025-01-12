import dotenv   
from langchain_openai import ChatOpenAI

dotenv.load_dotenv() # Load environment variables from .env file


chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)