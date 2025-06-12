# import requests
# import os

# class LLMService:
#     def __init__(self):
#         self.api_key = os.getenv("HUGGINGFACE_API_KEY")
#         self.model_name = "mistralai/Mistral-7B-Instruct-v0.3"  
#         self.api_url = f"https://api-inference.huggingface.co/models/{self.model_name}"
#         self.headers = {
#             "Authorization": f"Bearer {self.api_key}",
#             "Content-Type": "application/json"
#         }

#     def generate_response(self, context: str, query: str) -> str:
#         prompt = f"""
#         Context: {context}
        
#         Customer Query: {query}
        
#         As a helpful customer service assistant for a mobile cover store, provide a helpful and accurate response:
#         """

#         payload = {
#             "inputs": prompt,
#             "parameters": {
#                 "temperature": 0.5,
#                 "max_new_tokens": 256,
#                 "do_sample": True
#             }
#         }

#         response = requests.post(self.api_url, headers=self.headers, json=payload)

#         if response.status_code == 200:
            

#             result = response.json()
#             # print(f"LLM response: {result}")
#             if isinstance(result, list) and "generated_text" in result[0]:
#                 return result[0]["generated_text"].strip()
#             elif isinstance(result, dict) and "generated_text" in result:
#                 return result["generated_text"].strip()
#             else:
#                 return "Unexpected response format."
#         else:
#             return f"Error {response.status_code}: {response.text}"


import requests
import os

def extract_clean_response(output_text: str) -> str:
        # Define where your actual answer should begin (based on your prompt design)
        response_markers = [
            "Answer ONLY with your response (no extra text):",
            "Now answer the question below.",
            "Provide a helpful, accurate, and domain-specific response:"
        ]

        # Try to extract the answer using known markers
        for marker in response_markers:
            if marker in output_text:
                output_text = output_text.split(marker)[-1].strip()
        
        # Final cleanup: remove any quotes or surrounding newlines
        cleaned = output_text.strip().strip('"').strip("'")
        
        return cleaned

class LLMService:
    def __init__(self):
        self.api_key = os.getenv("HUGGINGFACE_API_KEY")
        self.model_name = "mistralai/Mistral-7B-Instruct-v0.3"
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_name}"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }


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

Do NOT provide any additional information or answers outside this scope.

Now answer the question below.

Context:
{context}

Customer Query:
{query}

Answer ONLY with your response (no extra text):
"""

        payload = {
            "inputs": prompt.strip(),
            "parameters": {
                "temperature": 0.2,
                "max_new_tokens": 256,
                "do_sample": False
            }
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            output_text = ""

            if isinstance(result, list) and "generated_text" in result[0]:
                output_text = result[0]["generated_text"]
            elif isinstance(result, dict) and "generated_text" in result:
                output_text = result["generated_text"]
            else:
                return "Unexpected response format."

            cleaned = extract_clean_response(output_text)

            return cleaned

        else:
            return f"Error {response.status_code}: {response.text}"
