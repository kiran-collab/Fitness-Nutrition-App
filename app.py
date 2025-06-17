import os
from dotenv import load_dotenv
import streamlit as st

from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain_community.document_loaders import TextLoader

# --- Load Environment Variables ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID")

# --- Sanity Checks ---
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY. Set it in .env.")
if not ASTRA_DB_APPLICATION_TOKEN or not ASTRA_DB_ID:
    raise ValueError("Missing Astra DB credentials. Set ASTRA_DB_APPLICATION_TOKEN and ASTRA_DB_ID in .env.")

# --- Initialize LLM and Embeddings ---
llm = OpenAI(temperature=0.5)
embedding = OpenAIEmbeddings()

# --- Load Knowledge Base ---
loader = TextLoader("fitness_knowledge_base.txt")
documents = loader.load()

# --- Setup Astra Vector Store ---
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")

vectordb = AstraDBVectorStore(
    embedding=embedding,
    collection_name="fitness_docs",
    token=ASTRA_DB_APPLICATION_TOKEN,
    api_endpoint=ASTRA_DB_API_ENDPOINT
)
vectordb.add_documents(documents)

# --- Retrieval Chain ---
retriever = vectordb.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# --- Agent Tools ---
nutrition_tool = Tool(
    name="NutritionAdvisor",
    func=qa_chain.run,
    description="Provides dietary and nutrition advice."
)

fitness_tool = Tool(
    name="WorkoutPlanner",
    func=qa_chain.run,
    description="Provides workout plans and fitness guidance."
)

agent = initialize_agent(
    tools=[nutrition_tool, fitness_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# --- Streamlit UI ---
st.set_page_config(page_title="AI Nutrition & Fitness Coach", layout="centered")
st.title("🏋️ AI-Powered Nutrition & Fitness Advisor")

query = st.text_input("Ask anything about fitness or diet:")

if query:
    with st.spinner("Thinking..."):
        response = agent.run(query)
        st.write("**Response:**")
        st.success(response)
