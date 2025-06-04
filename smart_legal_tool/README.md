# ⚖️ Smart Legal QA Search Engine (CLI Version)

A command-line based legal question-answering tool that enables users to ask plain-language questions 
about legal documents (such as contracts, NDAs, and privacy policies). Powered by LangChain, OpenAI's GPT, 
and Hugging Face embeddings.

---

## 📚 Project Overview

This project demonstrates how to combine natural language processing and vector search to build a smart 
legal assistant. Users can query structured legal text in natural English, and the system returns accurate 
answers along with document context.

---

## 🧠 Key Features

- ✅ **CSV Document Loader**: Loads legal texts from structured CSV files
- 🧩 **Text Chunking**: Splits long text into overlapping chunks for better retrieval
- 🔍 **Semantic Search**: Retrieves relevant sections using Hugging Face embeddings
- 🧠 **LLM-Powered Answers**: Uses GPT-4o-mini (or another OpenAI model) to answer questions
- 🧪 **Interactive CLI**: Accepts user queries in a loop; type `exit` to quit

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (set in `.env` file as `OPENAI_API_KEY`)
- Required Python packages (see `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/smart-legal-qa.git
   cd smart-legal-qa
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt\
   ```

4. Set your OpenAIAPI key in a .env file:

   OPENAI_API_KEY=your_openai_api_key_here
---

## 🧑‍💻 Usage

Run the CLI application by executing the following command in your terminal:

   ```bash
   python app.py
   ```

You'll be prompted to enter your questions about the legal documents.

Type your query and press Enter.
Type exit to quit the program.

## 💬 Example Queries You Can Try

- "What is the employment classification of Emily Reyes?"
- "How long is the non-compete clause in effect after Raj leaves?"
- "What benefits is Raj Malhotra entitled to?"
- "What is the length of the probationary period in Jordan’s contract?"


## 📇 Connect with me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/michael-carrington-a34314368)


