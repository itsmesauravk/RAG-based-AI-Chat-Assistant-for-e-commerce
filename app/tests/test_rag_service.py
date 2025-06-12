import pytest
from app.services.rag_service import RAGService

def test_product_query():
    rag_service = RAGService()
    response = rag_service.get_response("Do you have iPhone 15 cases?")
    assert "iPhone 15" in response

def test_policy_query():
    rag_service = RAGService()
    response = rag_service.get_response("What is your return policy?")
    assert len(response) > 0