from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = SimpleDirectoryReader('docs').load_data()
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

