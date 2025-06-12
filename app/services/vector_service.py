# import pinecone
# from sentence_transformers import SentenceTransformer
# import json
# from typing import List, Dict
# import os

# class VectorService:
#     def __init__(self):
#         self.model = SentenceTransformer('all-MiniLM-L6-v2')
#         self.index_name = "mobile-cover-store"
#         self.index = None

#     def setup_pinecone(self):
#         pinecone.init(
#             api_key=os.getenv("PINECONE_API_KEY"),
#             environment=os.getenv("PINECONE_ENVIRONMENT")
#         )
#         # Create index if not exists
#         if self.index_name not in pinecone.list_indexes():
#             pinecone.create_index(self.index_name, dimension=384)
#         self.index = pinecone.Index(self.index_name)

#     def create_embeddings(self, texts: List[str]) -> List[List[float]]:
#         return self.model.encode(texts).tolist()

#     def upsert_documents(self, documents: List[Dict]):
#         """
#         Upserts documents into Pinecone index.
#         Each document must have a unique 'id' and a 'text' field.
#         Optionally include 'metadata'.
#         """
#         # Ensure Pinecone index is ready
#         if not self.index:
#             self.setup_pinecone()

#         vectors = []
#         for doc in documents:
#             text = doc['text']
#             vector = self.create_embeddings([text])[0]
#             vector_id = doc['id']
#             metadata = doc.get('metadata', {})
#             vectors.append((vector_id, vector, metadata))

#         self.index.upsert(vectors)
#         print(f"Upserted {len(vectors)} documents into Pinecone.")

#     def search_similar(self, query: str, top_k: int = 5):
#         """
#         Search Pinecone for documents similar to the query.
#         Returns list of matched documents with metadata and scores.
#         """
#         # Ensure Pinecone index is ready
#         if not self.index:
#             self.setup_pinecone()

#         query_vector = self.create_embeddings([query])[0]
#         results = self.index.query(
#             vector=query_vector,
#             top_k=top_k,
#             include_metadata=True
#         )

#         return results['matches']




from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
import os
from typing import List, Dict
from dotenv import load_dotenv
load_dotenv()



class VectorService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index_name = "mobile-cover-store"
        self.dimension = 384  # All-MiniLM-L6-v2 output dimension
        self.pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index = None
        self.setup_pinecone()

    def setup_pinecone(self):

        # Delete the old index if exists
        # if self.index_name in self.pinecone.list_indexes().names():
        #     print(f"Deleting old index: {self.index_name}")
        #     self.pinecone.delete_index(self.index_name)

        # Create index if it doesn't exist
        if self.index_name not in self.pinecone.list_indexes().names():
            self.pinecone.create_index(
                name=self.index_name,
                dimension=self.dimension,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",  # or gcp
                    region=os.getenv("PINECONE_REGION", "us-east-1")
                )
            )

        self.index = self.pinecone.Index(self.index_name)

    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        return self.model.encode(texts).tolist()

    def upsert_documents(self, documents: List[Dict]):
        vectors = []
        for doc in documents:
            text = doc['text']
            vector = self.create_embeddings([text])[0]
            vector_id = doc['id']
            metadata = doc.get('metadata', {})
            vectors.append((vector_id, vector, metadata))

        self.index.upsert(vectors)
        

    def search_similar(self, query: str, top_k: int = 5):
        query_vector = self.create_embeddings([query])[0]
        results = self.index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True
        )
        return results['matches']
