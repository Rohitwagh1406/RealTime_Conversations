from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

# os.environ["GROQ_API_KEY"] = "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"

def batch():
    chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", groq_api_key=os.getenv("GROQ_API_KEY"))

    system = "You are a helpful assistant."
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt | chat
    print(chain.invoke({"text": "Explain the importance of low latency LLMs."}))

# Streaming
def streaming():
    chat = ChatGroq(temperature=0, model_name="llama2-70b-4096",groq_api_key=os.getenv("GROQ_API_KEY"))
    prompt = ChatPromptTemplate.from_messages([("human", "Write a very long poem about {topic}")])
    chain = prompt | chat
    for chunk in chain.stream({"topic": "The Moon"}):
        print(chunk.content, end="", flush=True)

# batch()
streaming()