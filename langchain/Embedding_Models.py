from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
## Single Document
result = embedding.embed_query("Delhi is the capital of India")

print(str(result))

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

## Multiple Documents

result = embedding.embed_documents(documents)

print(str(result))

## Opensource Embeddings
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

vector = embedding.embed_documents(documents)

print(str(vector))
