from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

# model = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     temperature=0.2,
#     max_tokens=256,
#     )

# result = model.invoke("can you tell me about Avengers Endgame?")

# print(result.content)


class LLMGeminiService:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.2,
            max_tokens=256,
        )

    def generate_response(self, context: str, query: str) -> str:
        prompt = f"""
You are Casemellow AI Assistant, a helpful customer support assistant for a mobile cover store.

You can ONLY answer questions about:
- Casemellow 
- Product details
- Order status
- Delivery info
- Return & refund policies
- Product compatibility (like iPhone model cases)

If asked anything else, reply EXACTLY with:
"I'm an AI assistant specifically built for Casemellow. I can't help with that topic."

Do NOT provide any additional information or answers outside this scope but you can give answers to the question like ['Hi', "Hello" ,"How are you?", "Thank you"] with the proper response to prompt them to view and buy our product.

Now answer the question below.

Context:
{context}

Customer Query:
{query}

Answer ONLY with your response (no extra text):
"""
        
        # print("Generated Prompt:", prompt.strip())
        
        response = self.model.invoke(prompt.strip())

        if response:
            return response.content.strip()
        else:   
            return "No response generated. Please try again later."