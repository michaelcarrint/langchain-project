# 🧠 Smart Study Assistant

A lightweight AI-powered tool designed to help students understand core 
concepts from their curriculum-based textbooks — starting with 
**Biology**.

> Built with LangChain, it enables textbook-level question answering using 
Retrieval-Augmented Generation (RAG), providing concise and sourced 
responses from long-form PDF content.

---

## ✅ Project Goal

To make it easier for students to explore and understand large textbooks 
by simply asking questions in natural language. The assistant returns 
answers with context directly from the material — like a smarter version 
of a study guide.

---

## ⚙️ Stack & Tools Used

- **LangChain** with `refine` chain (previously tested with `stuff`)
- **Chroma** as the vector store
- **HuggingFace** embedding model: `all-MiniLM-L6-v2`
- **OpenAI** for LLM responses: `gpt-4o-mini`
- **PDF documents** as input (tested on a full Biology textbook, ~189 
pages)
- Built and tested in **Jupyter Notebook** (Python)

---

## 🧪 Why I Chose `refine` Chain

Given the large size of the textbook, I tested both chain types:

- `stuff`: Works well for short documents; uses a single prompt.
- `refine`: Better suited for long-form content. It generates an initial 
answer from the first chunk and then refines it with additional chunks.

Using `refine` helped preserve coherence and factual grounding across 
large amounts of context.

---

## 📝 How It Works

1. PDF textbook is split into text chunks
2. Each chunk is embedded and stored in Chroma DB
3. User asks a question
4. The system retrieves relevant chunks
5. The `refine` chain generates a concise answer using retrieved context

---

## 📌 Example Query

```python
question = "Was cell discussed in this textbook?"
result = qa_chain({"query": question})
print(result["result"])

## 🧩 Features & Next Steps

- ✅ PDF-based textbook ingestion  
- ✅ Retrieval-based QA with contextual grounding  
- ⏳ Show source page numbers for traceability  
- ⏳ Add conversational memory to simulate tutoring  
- ⏳ Expand beyond Biology — support other subjects  
- ⏳ Support diagrams/images (multimodal)  
- ⏳ Build a simple UI or web app  
- ⏳ Explore local curriculum integration  

---

## 🚀 Vision

This project began as an educational tool, but there's potential to turn 
it into a full-fledged MVP — possibly integrated into tools like 
**FlexiSAF** to support students across Nigeria with locally relevant, 
AI-powered learning companions.

## 📚 Textbook Licensing

This project includes *GeneralBiology-2.pdf*, a textbook licensed under 
the GNU Lesser General Public License v3.0.  
You are free to share and modify the material under the same license 
terms.

For full license details, see the [LICENSE](./LICENSE) file or visit 
[gnu.org/licenses/lgpl-3.0](https://www.gnu.org/licenses/lgpl-3.0.txt).

