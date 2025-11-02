# 🤖 Telegram ChatGPT Bot

A simple Telegram bot built using **Python**, **Aiogram**, and **OpenAI's GPT model** that allows you to chat directly with ChatGPT through Telegram.  
This bot supports clearing previous conversation context and provides basic help commands.

---

## 🚀 Features

- 💬 Chat with ChatGPT (using `gpt-3.5-turbo`)
- 🧠 Maintains conversation context between messages
- 🧹 `/clear` command to reset the chat context
- 🆘 `/help` and `/start` commands for quick usage help
- 🔐 Environment variables support via `.env` file

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Aiogram** – for handling Telegram bot updates
- **OpenAI API** – for generating responses
- **python-dotenv** – for loading environment variables

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/telegram-chatgpt-bot.git
cd telegram-chatgpt-bot

python -m venv venv
venv\Scripts\activate       # On Windows


OPENAI_API_KEY=your_openai_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
