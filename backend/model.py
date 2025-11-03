import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
import gdown
from langchain_community.embeddings import SentenceTransformerEmbeddings

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")    
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "db")


#Ensure API key is set
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not found in .env")

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = Chroma(
    persist_directory=CHROMA_DB_PATH,
    embedding_function=embeddings   
)
retriever = vector_db.as_retriever()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
)

qa_chain = load_qa_chain(
    llm=llm,
    chain_type="stuff",
)

def get_response(query):
    docs = retriever.get_relevant_documents(query)
    return qa_chain.run(input_documents=docs, question=query)