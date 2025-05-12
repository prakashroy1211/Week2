from chromadb import Client
from chromadb.config import Settings

# Initialize ChromaDB client with default settings (in-memory DB)
client = Client(Settings())

# Create or get a collection
collection = client.get_or_create_collection(name="my_collection")

# Add a sample document
collection.add(
    documents=["This is a sample document about natural language processing."],
    metadatas=[{"source": "intro"}],
    ids=["doc1"]
)

# Query the database
results = collection.query(
    query_texts=["language processing"],
    n_results=1
)

# Print the result
print("Query result:", results)