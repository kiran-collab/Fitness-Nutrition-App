# 🏋️ AI-Powered Fitness & Nutrition Advisor

A multi-agent Streamlit application that helps users make smarter health decisions using Retrieval-Augmented Generation (RAG), LangChain tools, Astra DB, and OpenAI models.

## 🚀 Features

- 🤖 Multi-agent system: Nutrition advisor, workout planner, and supplement suggester  
- 📚 Document-grounded responses using `fitness_knowledge_base.txt`  
- 🧠 LangGraph integration for workflow orchestration  
- 🔍 Langfuse tracing for observability  
- 📊 RAGAS evaluation for faithfulness and answer quality  
- 📦 Fully Dockerized and deployable anywhere  

## 🧠 Tech Stack

- Streamlit – User interface  
- LangChain, LangGraph – Multi-agent workflows  
- Astra DB (via langchain-astradb) – Vector database  
- OpenAI – LLM for reasoning and response generation  
- Langfuse – Tracing and logging  
- RAGAS – RAG pipeline evaluation  

## 🗂️ Project Structure

```
fitness-agent-app/
├── app.py                    # Streamlit app logic
├── workflow.py              # LangGraph workflow setup
├── eval_ragas.py            # Evaluate output quality using RAGAS
├── fitness_knowledge_base.txt  # Domain content used for vector search
├── eval_dataset.json        # RAGAS-compatible eval dataset
├── .env                     # Environment config (OpenAI, Astra keys)
├── requirements.txt         # Python dependencies
├── Dockerfile               # Build container
├── docker-compose.yml       # Simplified deployment
└── README.md                # Project overview
```

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/fitness-agent-app.git
cd fitness-agent-app
```

### 2. Install Dependencies

```
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file:

```
OPENAI_API_KEY=sk-...
ASTRA_DB_APPLICATION_TOKEN=AstraCS:...
ASTRA_DB_ID=your-db-id
ASTRA_DB_API_ENDPOINT=https://your-db-id-region.apps.astra.datastax.com
```

### 4. Run the App

```
streamlit run app.py
```

## 🐳 Docker Instructions

Build and run with Docker:

```
docker-compose up --build
```

## 🔬 Evaluation with RAGAS

Evaluate your app's faithfulness and answer quality:

```
python eval_ragas.py
```

## 🧪 Sample Questions

- “What should I eat post-workout?”  
- “Give me a 5-day beginner gym plan.”  
- “What supplements improve muscle gain?”

## 🔐 Environment Variables

| Key                         | Description                           |
|----------------------------|---------------------------------------|
| OPENAI_API_KEY             | OpenAI or Claude API key              |
| ASTRA_DB_APPLICATION_TOKEN | Astra DB token with DB admin rights   |
| ASTRA_DB_ID                | Your Astra database UUID              |
| ASTRA_DB_API_ENDPOINT      | Full URL of Astra DB instance         |

## 📌 Future Enhancements

- Pinecone/FAISS fallback  
- Langflow visual designer  
- Auth + user feedback loop  
- Mobile view optimization
