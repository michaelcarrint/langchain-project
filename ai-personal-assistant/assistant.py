
import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

# LangChain Components
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm = llm,
    memory = memory,
    verbose = True
)
print("👋 Hi there, I am your personal Assistant, Enter 'exit', to stop\n")


while True:
    user_input = input("> ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye✌️")
        break
response = conversation.predict(input=user_input)
print("🤖Personal Assistant\n\n", response)
