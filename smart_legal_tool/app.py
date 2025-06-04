
import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

from langchain.document_loaders import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

loader = CSVLoader(file_path="legal_smart_document.csv")
docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
split_docs = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = DocArrayInMemorySearch.from_documents(split_docs, embeddings)

retriever = vectorstore.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

import time

print("Ask your questions (type 'exit' to quit)")


while True:
    user_input = input("Enter your query: ").strip()
    if not user_input:
        print("please enter a query")
        continue
    if user_input.lower() == 'exit':
        print("exiting....")
        time.sleep(5)
        print("exited")
        break
    
    response = qa_chain.invoke({"query": user_input})
    print(" ")
    print(response["result"])
    print("-" * 40)
