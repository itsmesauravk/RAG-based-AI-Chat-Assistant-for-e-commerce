

# import json
# from app.services.vector_service import VectorService

# def ingest_products():
#     print("📦 Ingesting products...")
#     vector_service = VectorService()

#     # Load products
#     with open('app/data/products.json', 'r') as f:
#         products = json.load(f)

#     # Create documents for vector store
#     documents = []
#     for product in products:
#         doc_text = f"{product['name']} {product['brand']} {product['price']} {', '.join(product['compatibility'])} {', '.join(product['features'])} {product['description']}"

#         documents.append({
#             'id': f"product-{product['id']}",
#             'text': doc_text,
#             'metadata': {
#                 "text": doc_text,
#                 "type": "product",
#                 "id": product["id"]
#             }
#         })

#     vector_service.upsert_documents(documents)
#     print(f"✅ Upserted {len(documents)} products")

# def ingest_policies():
#     print("📜 Ingesting policies...")
#     vector_service = VectorService()

#     # Load policy text file
#     with open("app/data/policies.txt", "r") as f:
#         content = f.read()

#     # Split into sections using headers like "Shipping:", "Returns:", etc.
#     sections = content.split("\n\n")
#     documents = []

#     for i, section in enumerate(sections):
#         if ':' in section:
#             title, body = section.split(":", 1)
#             text = f"{title.strip()}: {body.strip()}"
#             documents.append({
#                 'id': f"policy-{i}",
#                 'text': text,
#                 'metadata': {
#                     "text": text,
#                     "type": "policy",
#                     "section": title.strip()
#                 }
#             })

#     vector_service.upsert_documents(documents)
#     print(f"✅ Upserted {len(documents)} policies")

# def ingest_faqs():
#     print("❓ Ingesting FAQs...")
#     vector_service = VectorService()

#     with open("app/data/faqs.txt", "r") as f:
#         lines = f.readlines()

#     documents = []
#     i = 0
#     while i < len(lines):
#         if lines[i].startswith("Q:") and (i + 1 < len(lines) and lines[i+1].startswith("A:")):
#             question = lines[i].strip()[3:]
#             answer = lines[i+1].strip()[3:]
#             full_text = f"Q: {question}\nA: {answer}"
#             documents.append({
#                 'id': f"faq-{i}",
#                 'text': full_text,
#                 'metadata': {
#                     "text": full_text,
#                     "type": "faq",
#                     "question": question
#                 }
#             })
#             i += 2
#         else:
#             i += 1

#     vector_service.upsert_documents(documents)
#     print(f"✅ Upserted {len(documents)} FAQs")

# if __name__ == "__main__":
#     ingest_policies()
#     ingest_faqs()
#     ingest_products()



import json
from app.services.vector_service import VectorService

def ingest_products():
    print("📦 Ingesting products...")
    vector_service = VectorService()

    # Load products
    with open('app/data/cleaned_products.json', 'r') as f:
        products = json.load(f)

    documents = []
    for product in products:
        # Compose the searchable text field for embedding
        
        doc_text = f"{product['name']} {product['brand']} {product['price']} {product['model']} {product['coverType']} {product['category']} {product['description']} {product['productLink']}"


        documents.append({
            'id': f"product-{product['id']}",
            'text': doc_text,
            'metadata': {
                "text": doc_text,
                "type": "product",
                "id": product["id"],
                "link": product["productLink"]
            }

        })

    vector_service.upsert_documents(documents)
    print(f"✅ Upserted {len(documents)} products")

def ingest_policies():
    print("📜 Ingesting policies...")
    vector_service = VectorService()

    with open("app/data/policies.txt", "r") as f:
        content = f.read()

    # Split by double newlines for sections
    sections = [sec.strip() for sec in content.split("\n\n") if sec.strip()]
    documents = []

    for i, section in enumerate(sections):
        # Optionally parse title:body if colon present
        if ':' in section:
            title, body = section.split(':', 1)
            text = f"{title.strip()}: {body.strip()}"
            metadata_section = title.strip()
        else:
            text = section
            metadata_section = "General"

        documents.append({
            'id': f"policy-{i}",
            'text': text,
            'metadata': {
                "text": text,
                "type": "policy",
                "section": metadata_section
            }
        })

    vector_service.upsert_documents(documents)
    print(f"✅ Upserted {len(documents)} policies")

def ingest_faqs():
    print("❓ Ingesting FAQs...")
    vector_service = VectorService()

    with open("app/data/faqs.txt", "r") as f:
        lines = f.readlines()

    documents = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("Q:") and (i + 1 < len(lines) and lines[i+1].startswith("A:")):
            question = lines[i].strip()[3:].strip()
            answer = lines[i+1].strip()[3:].strip()
            full_text = f"Q: {question}\nA: {answer}"
            documents.append({
                'id': f"faq-{i}",
                'text': full_text,
                'metadata': {
                    "text": full_text,
                    "type": "faq",
                    "question": question
                }
            })
            i += 2
        else:
            i += 1

    vector_service.upsert_documents(documents)
    print(f"✅ Upserted {len(documents)} FAQs")

if __name__ == "__main__":
    ingest_policies()
    ingest_faqs()
    ingest_products()
