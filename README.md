# 🌦️ Weather Agent (LangChain + Gemini)

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agent-green)](https://python.langchain.com/)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange)](https://ai.google.dev/)
[![OpenWeather](https://img.shields.io/badge/OpenWeather-API-yellow)](https://openweathermap.org/api)
[![SQLite](https://img.shields.io/badge/SQLite-Checkpoint%20Memory-003B57)](https://www.sqlite.org/index.html)

A CLI weather assistant built with LangChain, Google Gemini, and OpenWeather. ☁️

## ✨ What it does

- 💬 Answers weather questions in natural language
- 🧰 Uses tools to:
  - 📍 detect your current city (`get_location`) when no city is provided
  - 🌡️ fetch current weather from OpenWeather (`get_weather`)
- 🗂️ Stores conversation checkpoints in SQLite (`db/checkpoints.db`)
- 🚫 Declines non-weather questions

## ✅ Requirements

- 🐍 Python 3.11+
- 🔑 Google AI API key (Gemini)
- 🔑 OpenWeather API key

## 🛠️ Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🔐 Environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_ai_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

If available, you can start from:

```bash
cp .env.example .env
```

## ▶️ Run

```bash
python main.py
```

When the app starts, it automatically creates the `db/` folder if it does not exist. 📁

Ask questions like:

- `What is the weather in Tokyo?`
- `How is the weather today?`

Type `exit` or `quit` to stop. 👋

## 🗃️ Data and git ignore

- SQLite checkpoints are stored in `db/checkpoints.db`
- `db/` and common SQLite file extensions are ignored in `.gitignore`

## 📝 Notes

- `main.py` logs a short prefix of the OpenWeather key for debugging
- Weather endpoint used: OpenWeather Current Weather API

---

<p align="center">
  Made with ❤️ using Python, LangChain, Gemini, and OpenWeather
</p>
