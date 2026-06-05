from os import getenv

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.postgres import PostgresSaver

from services.weather_tools import get_location, get_weather

load_dotenv()


SYSTEM_PROMPT = """
You are a helpful assistant that provides weather information.
YOUR WORKFLOW:
    1. If the user asks for the weather without specifying a location, use the get_location tool
    2. Use the get_weather tool to fetch the weather information for the specified location.
    3. Answer a tip based on the weather conditions. For example, if it's sunny,
       you might say "It's a great day to go outside!" If it's rainy, you might say "Don't forget your umbrella!", and so on, and a tip about the vest they should wear. For example, if it's cold, you might say "Make sure to wear a warm vest!" If it's hot, you might say "A light vest would be perfect for today!"
Everything asked that's not related to the weather, location or trying to certfied that's the information is correct should be politely declined with a message like "I'm here to help with weather information. Please ask about the weather!"
"""

SUPERBASE_DB_URI = getenv("SUPERBASE_DB_URI")

if not SUPERBASE_DB_URI:
    raise ValueError("SUPERBASE_DB_URI environment variable is required")

connection = PostgresSaver.from_conn_string(SUPERBASE_DB_URI)
checkpointer = connection.__enter__()
checkpointer.setup()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
agent = create_agent(
    model=llm,
    tools=[get_weather, get_location],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)


def invoke_agent(user_message, thread_id):
    return agent.invoke(
        {
            "messages": [{"role": "user", "content": user_message}],
        },
        {
            "configurable": {
                "thread_id": thread_id,
            },
        },
    )
