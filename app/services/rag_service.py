from .vector_service import VectorService
from .llm_service import LLMService
from .llm_gemini_service import LLMGeminiService

class RAGService:
    def __init__(self):
        self.vector_service = VectorService()
        # self.llm_service = LLMService()                  # Not using this because of limited inference from HuggingFace API
        self.llm_gemini_service = LLMGeminiService()       # Using Gemini LLM for unlimited inference capabilities

    def get_response(self, query: str) -> str:
        # 1. Search for relevant documents
        relevant_docs = self.vector_service.search_similar(query)

        # 2. Create context from retrieved documents
        context = self._create_context(relevant_docs)

        # 3. Generate response using LLM
        # response = self.llm_gemini_service.generate_response(context, query)
        response = self.llm_gemini_service.generate_response(context, query)

        return response

    def _create_context(self, docs) -> str:
        """
        Combines the text of top-k retrieved documents into a single context string.
        """
        context_chunks = []
        for doc in docs:
            if "metadata" in doc and "text" in doc["metadata"]:
                context_chunks.append(doc["metadata"]["text"])
            elif "text" in doc:
                context_chunks.append(doc["text"])
        return "\n\n".join(context_chunks)
