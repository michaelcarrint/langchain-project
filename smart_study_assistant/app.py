import os 
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.environ['OPENAI_API_KEY']

from langchain_chroma import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

persist_directory = "book/project/"

vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model
)

# Initial prompt — for the first chunk
initial_prompt = PromptTemplate.from_template("""
Use the following context to answer the question.
If you don't know the answer, just say you don't know. Keep it concise.
Always end with: "thanks for asking!"

Context:
{context_str}

Question: {question}
Answer:
""")


refine_prompt = PromptTemplate.from_template("""
You have an existing answer:
{existing_answer}

Here is more context to consider:
{context_str}

Improve the original answer if needed. If not, return the original.
Remember: be concise, and end with "thanks for asking!"
""")


# Now create the refine QA chain with prompts
qa_mr = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    chain_type="refine",
    chain_type_kwargs={
        "question_prompt": initial_prompt,
        "refine_prompt": refine_prompt
    }
)

question = "was photosynthesis discussed in this textbook"
result = qa_mr({"query": question})
result["result"]
