from os import getenv, makedirs

import requests


def ensure_db_folder() -> None:
    """Create the local database folder when it does not exist."""
    makedirs("db", exist_ok=True)


def get_weather(city: str) -> str:
    """Return current weather details for the provided city name."""
    api_key = getenv("OPENWEATHER_API_KEY")
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"{city}: {description}, {temperature}°C"
    return f"Weather data for {city} is not available."


def get_location() -> str:
    """Return city name inferred from the current public IP address."""
    city = "Unknown"
    response = requests.get(
        "https://ipinfo.io/json", headers={"User-Agent": "weather-agent/1.0"}
    )

    if response.status_code == 200:
        data = response.json()
        city = data.get("city", "Unknown")
    return city
