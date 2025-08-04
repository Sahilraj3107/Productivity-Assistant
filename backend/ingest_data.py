import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import gdown
from langchain_community.embeddings import SentenceTransformerEmbeddings

# https://drive.google.com/file/d/1WOKUrk5gCQpoedMQ_XksrSPLcFymVPnj/view?usp=sharing
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

# Load Document
documents = [
    Document(page_content="Meeting notes : Discuss project X deliverables."),
    Document(page_content="Reminder: Submit report by Friday."),
    Document(page_content="Upcoming event: Tech conference next Wednesday."),
]

# Creating Embeddings
# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/embedding-001",
#     google_api_key=GEMINI_API_KEY,
#     request_timeout=120, 
# )
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

