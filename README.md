# RAG Chatbot Assistant - Casemellow

An intelligent AI-powered customer support assistant for Casemellow, a mobile cover e-commerce store. This chatbot leverages Retrieval-Augmented Generation (RAG) to provide accurate, context-aware responses to customer queries about products, policies, orders, and more.

## 🌟 Features

- **RAG Pipeline**: Advanced retrieval system using vector search for contextually relevant responses
- **Multi-LLM Support**: Integration with both HuggingFace Mistral-7B and Google Gemini APIs
- **Smart Product Search**: Intelligent product discovery and recommendation system
- **Policy Integration**: Comprehensive knowledge of return policies, shipping, and FAQs
- **Real-time Chat**: Fast, responsive customer support experience
- **Link Generation**: Automatic product link parsing with clickable responses
- **Scalable Architecture**: Built with FastAPI for high performance and scalability
- **Modern Frontend**: Clean, responsive UI built with Next.js and Tailwind CSS
- **Docker Support**: Containerized deployment for easy scaling and management

## 🛠️ Tech Stack

### Backend

- **Python 3.8+** - Core programming language
- **FastAPI** - High-performance web framework
- **LangChain** - LLM orchestration and chaining
- **Pinecone** - Vector database for embeddings
- **Pydantic** - Data validation and serialization
- **HuggingFace Transformers** - Model integration
- **Google Gemini API** - Advanced language model

### Frontend

- **Next.js** - React framework
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework

### Infrastructure

- **Docker** - Containerization
- **Render** - Cloud deployment platform
- **DockerHub** - Container registry

## 📁 Project Structure

```
rag-chat-assistant-casemellow/
├── app/
│   ├── main.py                    # FastAPI application entry point
│   ├── __init__.py
│   │
│   ├── data/                      # Data files and knowledge base
│   │   ├── cleaned_products.json  # Processed product catalog
│   │   ├── faqs.txt              # Frequently asked questions
│   │   ├── phone_cases.json      # Phone case inventory
│   │   ├── policies.txt          # Store policies and terms
│   │   └── products.json         # Raw product data
│   │
│   ├── models/                    # Data models and schemas
│   │   ├── schemas.py            # Pydantic models
│   │   └── __init__.py
│   │
│   ├── services/                  # Business logic and services
│   │   ├── llm_gemini_service.py # Gemini API integration
│   │   ├── llm_service.py        # HuggingFace LLM service
│   │   ├── rag_service.py        # RAG pipeline implementation
│   │   ├── vector_service.py     # Vector database operations
│   │   └── __init__.py
│   │
│   ├── tests/                     # Test suites
│   │   ├── test_api.py           # API endpoint tests
│   │   ├── test_rag_service.py   # RAG service tests
│   │   └── __init__.py
│   │
│   └── utils/                     # Utility functions
│       ├── modify_cases.py       # Data preprocessing utilities
│       └── __init__.py
│
├── scripts/
│   └── ingest_data.py            # Data ingestion script
│
├── .env.sample                   # Environment variables template
├── .env                          # Environment variables (not in repo)
├── Dockerfile                    # Docker configuration
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
├── .dockerignore               # Docker ignore rules
└── README.md                   # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerized deployment)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/itsmesauravk/RAG-based-AI-Chat-Assistant-for-e-commerce.git
cd RAG-based-AI-Chat-Assistant-for-e-commerce
```

### 2. Environment Setup

#### Create a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory using `.env.sample` as a template:

```bash
cp .env.sample .env
```

Add your API keys and configuration:

```env
# LLM API Keys
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here

# Vector Database
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=your_pinecone_environment
PINECONE_INDEX_NAME=your_index_name


```

### 4. Data Ingestion (Optional)

If you want to upload your own data to the vector database:

1. Place your data files in the `app/data/` directory
2. Update the file paths in `scripts/ingest_data.py`
3. Run the ingestion script:

```bash
python -m scripts.ingest_data
```

### 5. Run the Application

#### Development Mode:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Production Mode:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 6. Access the Application Locally

- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Docker Deployment

### Build and Run with Docker

```bash
# Build the Docker image
docker build -t casemellow-chatbot .

# Run the container
docker run -p 8000:8000 --env-file .env casemellow-chatbot
```

### Docker Compose (Recommended)

```yaml
version: "3.8"
services:
  chatbot:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    restart: unless-stopped
```

```bash
docker-compose up -d
```

## API Documentation

### Core Endpoints

#### Chat Endpoint

```http
POST /chat
Content-Type: application/json

{
  "message": "What phone cases do you have for iPhone 14?",
  "session_id": "001"
}
```

#### Health Check

```http
GET /health
```

### Example Response

```json
{
  "response": "We have several iPhone 14 cases available including clear cases, leather cases, and rugged protection cases. Here are some popular options: [Product Link](https://casemellow.com/iphone-14-cases)"
}
```

## Configuration

### Environment Variables

| Variable               | Description                          | Required | Default |
| ---------------------- | ------------------------------------ | -------- | ------- |
| `HUGGINGFACE_API_KEY`  | HuggingFace API key for model access | Yes      | -       |
| `GEMINI_API_KEY`       | Google Gemini API key                | Yes      | -       |
| `PINECONE_API_KEY`     | Pinecone vector database API key     | Yes      | -       |
| `PINECONE_ENVIRONMENT` | Pinecone environment region          | Yes      | -       |
| `PINECONE_INDEX_NAME`  | Name of your Pinecone index          | Yes      | -       |

### Model Configuration

The application supports multiple LLM providers. You can switch between them by modifying the service configuration in `app/services/rag_service.py`.

## Deployment

### Deploy to Render

1. Connect your GitHub repository to Render
2. Set environment variables in Render dashboard
3. Use the following build and start commands:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://langchain.com/) for the RAG framework
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Pinecone](https://pinecone.io/) for vector database services
- [HuggingFace](https://huggingface.co/) for model hosting
- [Google](https://ai.google.dev/) for Gemini API access

---

For more information, visit my [documentation](https://github.com/itsmesauravk/RAG-based-AI-Chat-Assistant-for-e-commerce/wiki) or check out the [live demo](https://your-demo-url.com).
