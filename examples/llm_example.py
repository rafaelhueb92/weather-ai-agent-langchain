from langchain_google_genai import ChatGoogleGenerativeAI
from os import getenv

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0.7, api_key=getenv("GOOGLE_API_KEY", "")
)

response = llm.invoke("What is the capital of France?")

print(response.content)
