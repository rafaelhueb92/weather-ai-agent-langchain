# 🌦️ Weather Agent (LangChain + Gemini)

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agent-green)](https://python.langchain.com/)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange)](https://ai.google.dev/)
[![OpenWeather](https://img.shields.io/badge/OpenWeather-API-yellow)](https://openweathermap.org/api)
[![SQLite](https://img.shields.io/badge/SQLite-Checkpoint%20Memory-003B57)](https://www.sqlite.org/index.html)

A weather assistant built with LangChain, Google Gemini, and OpenWeather, available in both CLI and web chat modes. ☁️

## ✨ What it does

- 💬 Answers weather questions in natural language
- 🧰 Uses tools to:
  - 📍 detect your current city (`get_location`) when no city is provided
  - 🌡️ fetch current weather from OpenWeather (`get_weather`)
- 🗂️ Stores conversation checkpoints in SQLite (`db/checkpoints.db`)
- 🌙 Includes a dark-themed web chat UI
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

### Web app

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

When the app starts, it automatically creates the `db/` folder if it does not exist. 📁

Ask questions like:

- `What is the weather in Tokyo?`
- `How is the weather today?`

Type `exit` or `quit` to stop. 👋

## 🗃️ Data and git ignore

- SQLite checkpoints are stored in `db/checkpoints.db`
- `db/` and common SQLite file extensions are ignored in `.gitignore`

## 📝 Notes

- `app.py` uses the configured LangChain weather agent from `agent.py`
- Flask static assets are served from `static/` and templates from `templates/`
- Weather endpoint used: OpenWeather Current Weather API

---

<p align="center">
  Made with ❤️ using Python, LangChain, Gemini, and OpenWeather
</p>
