# 🌦️ Weather Agent (LangChain + Gemini)

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Agent-green)](https://python.langchain.com/)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange)](https://ai.google.dev/)
[![OpenWeather](https://img.shields.io/badge/OpenWeather-API-yellow)](https://openweathermap.org/api)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Checkpoint%20Memory-336791)](https://www.postgresql.org/)

A weather assistant built with LangChain, Google Gemini, and OpenWeather, available in both CLI and web chat modes. ☁️

<div align="center" style="display: flex; justify-content: space-around;">
  <img src="images/print_sp_ny.png" alt="First" width="60%" height="60%">
</div>

## ✨ What it does

- 💬 Answers weather questions in natural language
- 🧰 Uses tools to:
  - 📍 detect your current city (`get_location`) when no city is provided
  - 🌡️ fetch current weather from OpenWeather (`get_weather`)
- 🗂️ Stores conversation checkpoints in PostgreSQL (configured via `SUPERBASE_DB_URI`)
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
SUPERBASE_DB_URI=postgresql://user:password@host:5432/database
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

Ask questions like:

- `What is the weather in Tokyo?`
- `How is the weather today?`

Type `exit` or `quit` to stop. 👋

## 🗃️ Checkpoints

- Conversation checkpoints are stored in PostgreSQL via `SUPERBASE_DB_URI`
- Ensure the PostgreSQL database is reachable before starting the app
- The agent initializes checkpoint tables automatically on startup

## 📝 Notes

- `app.py` uses the configured LangChain weather agent from `agent.py`
- Flask static assets are served from `static/` and templates from `templates/`
- Weather endpoint used: OpenWeather Current Weather API

---

<p align="center">
  Made with ❤️ using Python, LangChain, Gemini, and OpenWeather
</p>
