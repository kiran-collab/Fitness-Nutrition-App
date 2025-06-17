from langgraph.graph import StateGraph
from langgraph.prebuilt import chat_agent_executor
from langchain.agents import Tool
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

# === Set up LLM and retriever ===
llm = OpenAI(temperature=0.5)
embedding = OpenAIEmbeddings()

retriever = AstraDBVectorStore(
    embedding=embedding,
    collection_name="fitness_docs",
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
    api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT")
).as_retriever()

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# === Define tools ===
tools = [
    Tool(name="NutritionTool", func=qa_chain.run, description="Answers nutrition and diet questions"),
    Tool(name="WorkoutTool", func=qa_chain.run, description="Answers workout or training queries")
]

# === LangGraph State Machine ===
graph = StateGraph()
graph.add_node("advisor", chat_agent_executor(tools, llm))
graph.set_entry_point("advisor")

# Compile graph to agent_executor
agent_executor = graph.compile()

# Example usage
if __name__ == "__main__":
    user_input = input("Ask your health-related question: ")
    result = agent_executor.invoke({"input": user_input})
    print("🤖 Agent Response:\n", result["output"])
