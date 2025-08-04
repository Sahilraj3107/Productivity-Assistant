import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.chat_models import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI 
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
import gdown
from langchain_community.embeddings import SentenceTransformerEmbeddings

file_id = "1WOKUrk5gCQpoedMQ_XksrSPLcFymVPnj"
url = f"https://drive.google.com/uc?id={file_id}"
output = ".env"

gdown.download(url, output, quiet=False)

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")    
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "db")


#Ensure API key is set
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not found in .env")

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = Chroma(
    persist_directory=CHROMA_DB_PATH,
    embedding_function=embeddings   
)
retriever = vector_db.as_retriever()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GEMINI_API_KEY,
)

qa_chain = load_qa_chain(
    llm=llm,
    chain_type="stuff",
)

def get_response(query):
    docs = retriever.get_relevant_documents(query)
    return qa_chain.run(input_documents=docs, question=query)