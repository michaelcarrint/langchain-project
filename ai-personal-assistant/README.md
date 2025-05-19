
# 🧠 AI Personal Assistant with Memory (LangChain + OpenAI)

A simple command-line AI assistant that **remembers your past messages during a session** using `ConversationBufferMemory` from LangChain. Perfect for experimenting with conversational memory in LLM-based applications.

---

## ✨ Features

- ✅ Remembers your name and preferences during the chat  
- 🧠 Uses LangChain's `ConversationBufferMemory` to store full dialogue context  
- 🤖 Powered by OpenAI's GPT-4 (via `langchain-openai`)  
- 💬 Natural, contextual responses that feel more human  
- ⚙️ Lightweight and easy to run locally  

> ⚠️ This project uses deprecated LangChain components (`ConversationChain`, `ConversationBufferMemory`) that still work in version 0.2.6. Update to the new memory system when you're ready.  

---

## 🧪 Example Conversation

You: My name is Bernard  
Assistant: Nice to meet you, Bernard!

You: What’s my name?  
Assistant: You said your name is Bernard.

You: I like black coffee.  
Assistant: Great! I’ll remember that you like black coffee.

---

### 1. Clone the Repository

```bash
git clone https://github.com/michaelcarrint/ai-personal-assistant.git
cd ai-personal-assistant

### 2. Set Up Environment Variables

Create a `.env` file in the project root with the following content:

OPENAI_API_KEY=your_openai_key_here

### 3. Install Dependencies

```bash
pip install -r requirements.txt

### 4. Run the Assistant
python assistant.py

## 🙌 Acknowledgements

- Andrew Ng for his excellent course, **LangChain for LLM Application Development**.  
- [LangChain Documentation](https://docs.langchain.com/)  
- [OpenAI](https://platform.openai.com/)

