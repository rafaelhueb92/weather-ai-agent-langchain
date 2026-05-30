# Weather Agent (LangChain + Gemini)

A simple CLI weather assistant built with LangChain and Google Gemini.

## What it does

- Answers weather questions in natural language.
- Uses tools to:
  - detect your current city (`get_location`) when you don’t provide one
  - fetch weather data from OpenWeather (`get_weather`)
- Declines non-weather questions.

## Requirements

- Python 3.11+
- A Google AI API key (for Gemini)
- An OpenWeather API key

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_ai_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

You can also copy from the example file if present:

```bash
cp .env.example .env
```

## Run

```bash
python main.py
```

Type your weather question (for example: `What’s the weather in Lisbon?`).
Type `exit` to quit.

## Notes

- `main.py` currently logs part of the OpenWeather key prefix for debugging.
- Weather source endpoint used: OpenWeather current weather API.
