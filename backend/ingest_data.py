import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import gdown
from langchain_community.embeddings import SentenceTransformerEmbeddings

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")    
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "db")

#Ensure API key is set
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not found in .env")

# Load Document
documents = [
    Document(page_content="Meeting notes : Discuss project X deliverables."),
    Document(page_content="Reminder: Submit report by Friday."),
    Document(page_content="Upcoming event: Tech conference next Wednesday."),
]

# Creating Embeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
)
docs = text_splitter.split_documents(documents)

vector_db = Chroma.from_documents(
    docs,
    embedding =embeddings,
    persist_directory=CHROMA_DB_PATH
)

print("Documents successfully indexed!")