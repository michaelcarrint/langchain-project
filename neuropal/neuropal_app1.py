import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

st.title("🧠 Neuropal Medical Assistant")

st.info("⚠️ Neuropal provides general medical information only. Please consult a healthcare professional for personal advice.")


if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

if "chain" not in st.session_state:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
    prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
Ytemplate = """
You are Neuropal — a compassionate, knowledgeable AI assistant specializing in medical and neurological topics. You engage users in thoughtful, respectful, and clear conversations, with the goal of helping them understand complex health-related information.

Your role:
- Communicate with warmth, professionalism, and empathy.
- Provide medically accurate, easy-to-understand explanations.
- Respect user privacy and never guess if you’re unsure.
- Encourage users to consult licensed medical professionals when necessary.
- Remember and consider key details the user shares during the conversation.
- Do not give medical diagnoses or treatment plans. Instead, guide users toward better understanding and encourage professional consultation.

Use the following conversation history to maintain context:

{history}

User: {input}
Neuropal:"""

    )
            
    st.session_state.chain = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        prompt=prompt,
        verbose=False
    )

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show welcome message if chat is empty
if not st.session_state.chat_history:
    st.markdown("👋 Hi, I am Neuropal, your smart buddy bot! Ask me anything.")

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.memory.clear()
    st.rerun()

# Function to handle user input and clear the box
def handle_input():
    user_input = st.session_state.input
    if user_input:
        st.session_state.chat_history.append({"role": "user", "message": user_input})
        response = st.session_state.chain.predict(input=user_input)
        st.session_state.chat_history.append({"role": "assistant", "message": response})
        st.session_state.input = ""  # reset input here safely

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['message']}")
    else:
        st.markdown(f"**Neuropal:** {chat['message']}")

# Input box with callback to handle input
st.text_input(
    "Your message:",
    key="input",
    on_change=handle_input,
    placeholder="Type here...",
   
)
