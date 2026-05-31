from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from os import getenv

import requests

load_dotenv()


def get_weather(city: str) -> str:
    """Get the current weather for a given location."""
    print(f"Fetching weather data for {city}...")
    api_key = getenv("OPENWEATHER_API_KEY")
    print(
        f"Using OpenWeather API key: {api_key[:4]}..."
    )  # Print only the first 4 characters for security
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    print(f"Weather API response status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"{city}: {description}, {temperature}°C"
    return f"Weather data for {city} is not available."


def get_location() -> str:
    """Get the current location. Use this when the user asks for the weather without specifying a location."""
    print("Getting current location...")

    city = "Unknown"
    response = requests.get(
        "https://ipinfo.io/json", headers={"User-Agent": "weather-agent/1.0"}
    )

    if response.status_code == 200:
        data = response.json()
        city = data.get("city", "Unknown")
    return city


system_prompt = """
You are a helpful assistant that provides weather information. 
YOUR WORKFLOW:
    1. If the user asks for the weather without specifying a location, use the get_location tool
    2. Use the get_weather tool to fetch the weather information for the specified location.
    3. Answer a tip based on the weather conditions. For example, if it's sunny, 
       you might say "It's a great day to go outside!" If it's rainy, you might say "Don't forget your umbrella!", and so on.
Everything asked that's not related to the weather should be politely declined with a message like "I'm here to help with weather information. Please ask about the weather!"
"""

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
agent = create_agent(
    model=llm, tools=[get_weather, get_location], system_prompt=system_prompt
)

if __name__ == "__main__":
    human_query = ""

    while human_query.lower().lstrip() != "exit":
        human_query = input("Ask about the weather: ")

        if human_query.lower().lstrip() != "exit":
            response = agent.invoke(
                {"messages": [{"role": "user", "content": human_query}]}
            )

            print(response["messages"][-1].content)
